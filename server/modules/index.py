from flask import Blueprint, request

from model.model import IvdMaterial
from utils.db import db

from sqlalchemy import and_, func

from utils.model_utils import model_to_dict
from utils.result import result_succ

index_router = Blueprint('index', __name__, url_prefix='/')


@index_router.route('/', methods=['GET'])
def index():
    conditions = []
    page = 1
    if 'page' in request.args:
        page = int(request.args.get('page'))
    count = 20
    if 'count' in request.args:
        count = int(request.args.get('count'))
    # interface categories: 1:complex，0:simple
    interface_type = 0
    if 'interface_type' in request.args:
        interface_type = request.args.get('interface_type')
    # material_id，0:default
    material_id = 0
    if 'material_id' in request.args:
        material_id = request.args.get('material_id')
    if material_id != 0:
        conditions.append(IvdMaterial.material_id == material_id)
    # search keyword
    keyword = None
    if 'keyword' in request.args:
        keyword = request.args.get('keyword')
    if keyword:
        conditions.append(IvdMaterial.title.like(f"%{keyword}%"))
        conditions.append(IvdMaterial.description.like(f"%{keyword}%"))
    offset = (page - 1) * count
    res_list = db.session.query(IvdMaterial) \
        .filter(and_(*conditions)) \
        .offset(offset) \
        .limit(count)
    total_items = db.session.query(func.count(IvdMaterial.id)).scalar()
    total_pages = (total_items / count) + 1
    ret_list = {
        'total_pages': total_pages,
        'page': page,
        'count': count,
        'result': model_to_dict(res_list)
    }
    return result_succ(ret_list)
