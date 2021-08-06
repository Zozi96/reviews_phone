from flask import Blueprint
from .endpoints import LoginUserView, SignupUserView

api = Blueprint('users', __name__, url_prefix='/api/users')

api.add_url_rule(
    '/signup',
    view_func=SignupUserView.as_view('signup'),
    methods=['POST']
)

api.add_url_rule(
    '/login',
    view_func=LoginUserView.as_view('login'),
    methods=['POST']
)
