from flask import Blueprint

from utils.result import result_succ

about_router = Blueprint('about', __name__, url_prefix='/about')


@about_router.route("/")
def about():
    return result_succ({
        'title': '',
        'description': '',
        'company': ''
    })
