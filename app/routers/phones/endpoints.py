from flask import request, jsonify
from flask.views import MethodView
from app.models.phones import Brand, Phone
from app.schemas.brands import brand_schema, brands_schema, params_brand_schema
from app.schemas.phones import phone_schema, params_phone_schema, list_phones_schema

class BrandCreateView(MethodView):
    def post(self):
        data = request.get_json()
        errors = params_brand_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        else:
            brand = Brand.create(data.get('name'), data.get('description'))
            return jsonify(brand_schema.dump(brand)), 201


class BrandListView(MethodView):
    def get(self):
        return jsonify(brands_schema.dump(Brand.get_all())), 200


class PhoneCreateView(MethodView):
    def post(self):
        data = request.get_json() 
        errors = params_phone_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        else: 
            phone = Phone.create(
                name=data.get('name'), 
                brand_id=data.get('brand'), 
                date_release=data.get('date_release')
            )
            return jsonify({
                'message': 'Phone successfully created',
                'data': phone_schema.dump(phone)
            }), 201

class PhoneListView(MethodView):
    def get(self):
        page = request.args.get('page', 1, type=int)
        order = request.args.get('order', 'asc', type=str)
        return jsonify(
            list_phones_schema.dump(
                Phone.get_all_paginate(order , page)
            )
        ), 200
