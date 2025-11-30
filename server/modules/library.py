from flask import Blueprint

from model.model import FvdMaterialLibrary
from utils.db import db
from utils.result import result_succ

library_router = Blueprint('library', __name__, url_prefix='/library')


@library_router.route('/', methods=['GET'])
def index():
    res_list = db.session.query(FvdMaterialLibrary) \
        .filter(FvdMaterialLibrary.is_deleted == 0) \
        .all()
    data_list = []
    data = {}
    for res in res_list:
        data['name'] = res.name
        data['description'] = res.description
        data_list.append(data)
    return result_succ(data_list)
