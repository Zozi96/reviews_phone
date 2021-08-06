from flask import request, jsonify
from flask.views import MethodView
from app.models.phones import Brand, Phone


class BrandCreateView(MethodView):
    def post(self):
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        if not name or not len(name) > 0:
            return jsonify(message="Name is required"), 400
        elif len(name) > 50:
            return jsonify(message="Name must be less than 50 characters"), 400

        if Brand.get_by_name(name):
            return jsonify(message="Name already exists"), 400

        brand = Brand.create(name, description)
        return jsonify({
            'message': 'Brand successfully created',
            'data': {
                'name': brand.name,
                'description': brand.description if brand.description else 'Description not registered'
            }
        }), 201


class BrandListView(MethodView):
    def get(self):
        return jsonify({
            'message': 'List of brands',
            'data': [{
                'id': brand.id,
                'name': brand.name,
                'description': brand.description if brand.description else 'Description not registered'
            } for brand in Brand.get_all()]
        })


class PhoneCreateView(MethodView):
    def post(self):
        data = request.get_json()
        name = data.get('name')
        brand_id = data.get('brand_id')
        date_release = data.get('date_release')
        if not name or not len(name) > 0:
            return jsonify(message="Name is required"), 400
        elif len(name) > 100:
            return jsonify(message="Name must be less than 100 characters"), 400
        elif not brand_id or not len(brand_id) > 0:
            return jsonify(message="Brand is required"), 400
        elif not date_release or not len(date_release) > 0:
            return jsonify(message="Date release is required"), 400
        elif not len(date_release) > 0 or not date_release:
            return jsonify(message="Date is required"), 400

        if Phone.get_by_name(name):
            return jsonify(message="Phone already exists"), 400

        phone = Phone.create(name, brand_id, date_release)

        return jsonify({
            'message': 'Phone successfully created',
            'data': {
                'name': phone.name,
                'brand_id': phone.brand_id,
                'date_release': phone.date_release
            }
        }), 201
