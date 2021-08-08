from flask import Flask
from .core import extensions
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
        extensions.db.init_app(app)
        extensions.migrate.init_app(app=app, db=extensions.db)
        extensions.bcrypt.init_app(app)
        extensions.ma.init_app(app)
        extensions.jwt.init_app(app)
    return app
