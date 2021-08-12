from app.core.extensions import ma
from app.models.reviews import Review
from marshmallow import fields, validate


class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Review


class ParamsReviewSchema(ma.Schema):
    phone = fields.Int(required=True, validate=validate.Length(min=1))
    text = fields.Str(required=True, validate=validate.Length(min=1))
    user = fields.Int(required=True, validate=validate.Length(min=1))


review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)
params_review_schema = ParamsReviewSchema()
