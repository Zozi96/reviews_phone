from flask import jsonify, request
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from app.models.users import User
from app.models.reviews import Review
from app.schemas.reviews import review_schema, params_review_schema, list_review_schema


class ReviewCreateView(MethodView):
    @jwt_required()
    def post(self):
        data = request.get_json()
        user = User.get_current_identity()
        errors = params_review_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        else:
            review = Review.create(
                user_id=user.id,
                phone_id=data.get('phone_id'),
                text=data.get('text'),
            )

            return jsonify(review_schema.dump(review)), 201


class ReviewsListView(MethodView):
    def get(self):
        data = list_review_schema.dump(Review.get_all())
        return jsonify(data), 200


class ReviewUserListView(MethodView):
    @jwt_required()
    def get(self):
        user = User.get_current_identity()
        data = list_review_schema.dump(
            Review.get_by_user(user.id)
        )
        return jsonify(data), 200
