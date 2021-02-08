from flask_restful import Api
from flask import Blueprint
from .resources.watcher import *


api_bp = Blueprint("api", __name__)
api = Api(api_bp)

api.add_resource(Watcher, "/test")

