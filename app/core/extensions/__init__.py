from flask_sqlalchemy import SQLAlchemy # ORM
from flask_migrate import Migrate # Database migration
from flask_bcrypt import Bcrypt # Password hashing
from flask_marshmallow import Marshmallow # Schema validation
from flask_jwt_extended import JWTManager # JSON Web Token

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
ma = Marshmallow()
jwt = JWTManager()
