from flask import Flask
from .core.extensions import db, bcrypt, jwt, ma
from .models import tables
from .routers import endpoints

app = Flask(__name__)

for table in tables:
    table


def create_app(config):
    app.config.from_object(config)
    for endpoint in endpoints:
        app.register_blueprint(endpoint)
    with app.app_context():
        db.init_app(app)
        db.create_all()
        bcrypt.init_app(app)
        ma.init_app(app)
        jwt.init_app(app)
    return app
