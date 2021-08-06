from .database import Database
from .security import Jwt


class BaseConfig:
    ENV = 'production'
    DEBUG = False
    TESTING = False


class Develop(BaseConfig, Database, Jwt):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///reviews.db'
    JWT_SECRET_KEY = 'my-precious'


environment = {
    'develop': Develop
}
