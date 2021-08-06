from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token
from app.models.users import User


class SignupUserView(MethodView):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not len(username) > 0:
            return jsonify(message="Username is required"), 400
        elif len(username) > 120:
            return jsonify(message="Username must be less than 120 characters"), 400
        if not email or not len(email) > 0:
            return jsonify(message="Email is required"), 400
        elif len(email) > 120:
            return jsonify(message="Email must be less than 120 characters"), 400
        if not password or not len(password) > 0:
            return jsonify(message="Password is required"), 400

        if User.get_by_username(username):
            return jsonify(message="Username already exists"), 409
        if User.get_by_email(email):
            return jsonify(message="Email already exists"), 409

        User.create(
            username=username,
            email=email,
            password=password
        )
        data_response = {
            'username': username,
            'email': email
        }
        return jsonify({
            'message': 'User created successfully',
            'data': [data_response]
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
