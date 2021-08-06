from .users import api as users_api
from .index import api as index_api
from .phones import api as phones_api

endpoints = [
    index_api,
    users_api,
    phones_api
]
