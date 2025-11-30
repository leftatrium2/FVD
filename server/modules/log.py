from flask import Blueprint

log_router = Blueprint('log', __name__, url_prefix='/log')


@log_router.route('/index', methods=['GET'])
def log_index():
    pass
