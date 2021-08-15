from app.core.extensions import ma
from app.models.phones import Phone
from .brands import BrandSchema
from marshmallow import fields, validate


class PhoneSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Phone

    id = ma.auto_field()
    brand_id = ma.auto_field()
    name = ma.auto_field()
    date_release = ma.auto_field()


class ParamsPhoneSchema(ma.Schema):
    def validate_name(value):
        if Phone.get_by_name(value):
            raise validate.ValidationError(
                'Phone with this name already exists.')

    brand = fields.Int(required=True)
    name = fields.Str(
        required=True, validate=validate.Length(min=1, max=100))
    date_release = fields.DateTime(format='%Y-%m-%d', required=True)


class ListPhonesSchema(ma.Schema):
    class Meta:
        model = Phone
    id = ma.Integer(dump_only=True)
    brand = fields.Nested(BrandSchema(only=('name',)))
    name = fields.Str(required=True, dump_only=True)
    date_release = fields.DateTime(format='%Y-%m-%d', dump_only=True)


phone_schema = PhoneSchema()
phones_schema = PhoneSchema(many=True)
params_phone_schema = ParamsPhoneSchema()
list_phones_schema = ListPhonesSchema(many=True)
