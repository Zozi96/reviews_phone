from app.core.extensions import ma
from app.models.phones import Phone
from marshmallow import fields, validate

class PhoneSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Phone

class ParamsPhoneSchema(ma.Schema):
    def validate_name(value):
        if Phone.get_by_name(value):
            raise validate.ValidationError('Phone with this name already exists.')

    brand = fields.Integer(required=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    date_release = fields.DateTime(format='%Y-%m-%d', required=True)

phone_schema = PhoneSchema()
phones_schema = PhoneSchema(many=True)
params_phone_schema = ParamsPhoneSchema()
