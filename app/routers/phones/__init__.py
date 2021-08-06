from flask import Blueprint
from . import endpoints

api = Blueprint('phones', __name__, url_prefix='/api/phones')

api.add_url_rule(
    '/brand/add',
    view_func=endpoints.BrandCreateView.as_view('create_brand'),
    methods=['POST']
)

api.add_url_rule(
    '/brand/all',
    view_func=endpoints.BrandListView.as_view('list_brands'),
    methods=['GET']
)
