from flask import jsonify
from flask.views import MethodView


class IndexView(MethodView):
    def get(self):
        return jsonify(message='Hello, World!')
