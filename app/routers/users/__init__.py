from flask import Blueprint
from . import endpoints

api = Blueprint('users', __name__, url_prefix='/api/users')

api.add_url_rule(
    '/signup',
    view_func=endpoints.SignupUserView.as_view('signup'),
    methods=['POST']
)

api.add_url_rule(
    '/all',
    view_func=endpoints.UserListView.as_view('all'),
    methods=['GET']
)

api.add_url_rule(
    '/get/<int:id>',
    view_func=endpoints.UserGetEdit.as_view('get'),
    methods=['GET']
)

api.add_url_rule(
    '/login',
    view_func=endpoints.LoginUserView.as_view('login'),
    methods=['POST']
)
