from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token, jwt_required
from app.models.users import User
from app.schemas import users


class SignupUserView(MethodView):
    def post(self):
        data = request.get_json()
        errors = users.params_user_schema.validate(data)
        if errors:
            return jsonify(message=errors), 400
        user = User.create(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password')
        )
        return jsonify({
            'message': 'User created successfully',
            'data': users.user_schema.dump(user)
        }), 201


class UserListView(MethodView):
    def get(self):
        return jsonify(
            users.users_schema.dump(
                User.get_all()
            )
        ), 200


class UserGetEdit(MethodView):
    def get(self, id):
        user = User.query.get_or_404(id)
        return jsonify(users.user_schema.dump(user)), 200


class LoginUserView(MethodView):
    def post(self):
        data = request.get_json()
        user = User.get_by_username(data.get('username'))
        error = users.params_user_login_schema.validate(data)
        if error:
            return jsonify(error), 400
        elif not user.check_password(data.get('password')):
            return jsonify(password=['Wrong password']), 400

        return jsonify({
            'username': user.username,
            'access_token': create_access_token(identity=user.id)
        }), 200


class CurrentUserView(MethodView):
    @jwt_required()
    def get(self):
        user = User.get_current_identity()
        return jsonify(logged_in_as=user.username), 200