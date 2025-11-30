from flask import Blueprint, request

async_routes_router = Blueprint('async-routes', __name__, url_prefix='/get-async-routes')


@async_routes_router.route('/', methods=['GET'])
def async_routes():
    pass
