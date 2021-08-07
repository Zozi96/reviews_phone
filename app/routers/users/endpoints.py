from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token
from app.models.users import User
from app.schemas.users import (
    user_schema, users_schema, params_user_schema, params_user_login_schema)


class SignupUserView(MethodView):
    def post(self):
        data = request.get_json()
        error = params_user_schema.validate(data)
        if error:
            return jsonify(message=error), 400
        user = User.create(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password')
        )
        return jsonify({
            'message': 'User created successfully',
            'data': user_schema.dump(user)
        }), 201


class UserListView(MethodView):
    def get(self):
        return jsonify(
            users_schema.dump(
                User.query.all()
            )
        ), 200


class UserGetEdit(MethodView):
    def get(self, id):
        user = User.query.get_or_404(id)
        return jsonify(user_schema.dump(user)), 200


class LoginUserView(MethodView):
    def post(self):
        data = request.get_json()
        user = User.get_by_username(data.get('username'))
        error = params_user_login_schema.validate(data)
        if error:
            return jsonify(error), 400
        elif not user.check_password(data.get('password')):
            return jsonify(password=['Wrong password']), 400

        return jsonify({
            'username': user.username,
            'access_token': create_access_token(identity=user.id)
        }), 200
