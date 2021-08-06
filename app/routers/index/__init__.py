from flask import Blueprint
from .endpoint import IndexView

api = Blueprint('index', __name__, url_prefix='/')

api.add_url_rule(
    '/',
    view_func=IndexView.as_view('index'),
    methods=['GET']
)
