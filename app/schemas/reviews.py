from marshmallow import fields, validate

from app.core.extensions import ma
from app.models.reviews import Review
from .phones import PhoneSchema
from .users import UserSchema


class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Review

class ListReviewSchema(ma.Schema):
    id = fields.Int(required=True, dump_only=True)
    phone = fields.Nested(PhoneSchema(only=('name',)))
    text = fields.Str(required=True, dump_only=True)
    user = fields.Nested(UserSchema(only=('username',)))

class ParamsReviewSchema(ma.Schema):
    phone_id = fields.Int(required=True)
    text = fields.Str(required=True, validate=validate.Length(min=1))
    


review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)
list_review_schema = ListReviewSchema(many=True)
params_review_schema = ParamsReviewSchema()
