
from app.core.extensions import ma
from app.models.users import User
from marshmallow import fields, validate, ValidationError


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('password',)


class ParamsUserSchema(ma.Schema):
    def username_validator(value):
        if User.get_by_username(value):
            raise ValidationError('Username already exists')

    def email_validator(value):
        if User.get_by_email(value):
            raise ValidationError('Email already exists')

    username = fields.Str(
        required=True,
        validate=validate.And(
            validate.Length(min=1, max=80),
            username_validator
        )
    )
    email = fields.Email(
        required=True,
        validate=validate.And(
            validate.Length(min=1, max=120),
            email_validator
        )
    )
    password = fields.Str(
        required=True,
        validate=validate.Length(min=1)
    )


user_schema = UserSchema()
users_schema = UserSchema(many=True)

params_user_schema = ParamsUserSchema()
