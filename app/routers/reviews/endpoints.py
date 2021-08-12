from flask import jsonify, request
from flask.views import MethodView

from app.schemas.reviews import review_schema, params_review_schema


class ReviewCreateView(MethodView):
    pass

