from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token
from app.models.users import User
from app.schemas.users import user_schema, params_user_schema


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


class LoginUserView(MethodView):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if not username or not len(username) > 0:
            return jsonify(message="Username is required"), 400
        if not password or not len(password) > 0:
            return jsonify(message="Password is required"), 400

        user = User.get_by_username(username)
        if not user or not user.check_password(password):
            return jsonify(message="Invalid username or password"), 401
        access_token = create_access_token(identity=user.id)

        return jsonify(access_token=access_token), 200
