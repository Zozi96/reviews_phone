from marshmallow import fields, validate
from app.core.extensions import ma
from app.models.phones import Brand


class BrandSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Brand
        fields = (
            'id', 
            'name', 
            'description'
        )
    

class ParamsBrandSchema(ma.Schema):
    def name_validator(value):
        if Brand.get_by_name(name=value):
            raise validate.ValidationError('Brand already exists')

    name = fields.Str(
        required=True, 
        validate=validate.And(
            validate.Length(min=1, max=50), 
            name_validator
        )
    )
    description = fields.Str()

brand_schema = BrandSchema()
brands_schema = BrandSchema(many=True)
params_brand_schema = ParamsBrandSchema()
