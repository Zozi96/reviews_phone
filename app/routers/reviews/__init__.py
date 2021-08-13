from flask import Blueprint
from . import endpoints

api = Blueprint('reviews', __name__, url_prefix='/api/reviews')

api.add_url_rule(
    '/create',
    view_func=endpoints.ReviewCreateView.as_view('create_review'),
    methods=['POST']
)

api.add_url_rule(
    '/all',
    view_func=endpoints.ReviewsListView.as_view('list_reviews'),
    methods=['GET']
)

api.add_url_rule(
    '/user/all',
    view_func=endpoints.ReviewUserListView.as_view('list_user_reviews'),
    methods=['GET']
)
