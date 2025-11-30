import json
import logging
from datetime import datetime

from flask import Blueprint, request
from sqlalchemy import and_, func

from crawler.crawler_factory import crawler
from model.model import FvdTaskList, FvdOnlineList
from task.task_const import TASK_EXECUTION_EXECUTE_MODE
from task.task_manager import g_task_manager
from utils import const
from utils.db import db
from utils.model_utils import model_to_dict
from utils.privileges_utils import check_is_login_from_header
from utils.result import result_succ, result_failure
from utils.task_utils import gen_task_id

task_router = Blueprint('task', __name__, url_prefix='/task')


@task_router.route('/index', methods=['GET'])
def task_index():
    conditions = []
    page = 1
    if 'page' in request.args:
        page = int(request.args.get('page'))
    count = 20
    if 'count' in request.args:
        count = int(request.args.get('count'))
    material_id = 0
    if 'material_id' in request.args:
        material_id = request.args.get('material_id')
    if material_id != 0:
        conditions.append(FvdTaskList.material_library_id == material_id)
    offset = (page - 1) * count
    res_list = db.session.query(FvdTaskList) \
        .filter(and_(*conditions)) \
        .offset(offset) \
        .limit(count)
    total_items = db.session.query(func.count(FvdTaskList.id)).scalar()
    total_pages = (total_items / count) + 1
    ret_list = {
        'total_pages': total_pages,
        'page': page,
        'count': count,
        'result': model_to_dict(res_list)
    }
    return result_succ(ret_list)


@task_router.route("/get", methods=['GET'])
def task_get():
    task = g_task_manager.get_task()
    if task:
        return result_succ(task)
    return result_failure(const.TASKMANAGER_GET_TASK_EMPTY, "TASKMANAGER_GET_TASK_EMPTY")


# 添加任务第一步
# 获取视频信息，以及显示视频内容
@task_router.route('/simple/first', methods=['POST'])
def simple_task_first():
    result = check_is_login_from_header(request)
    if result != const.GLOBAL_SUCC:
        return result_failure(result, "error in check_is_login_from_header")
    req_json_str = request.data
    req_json = json.loads(req_json_str)
    url = None
    if 'url' in req_json:
        url = req_json['url']
    if not url:
        return result_failure(const.SIMPLE_TASK_FIRST_ERR_URL_EMPTY, "TASK_FIRST_ERR_URL_EMPTY")
    info = crawler.gen_info(url=url)
    if info:
        info_dict = info.info(url=url)
        if info_dict:
            info_dict_result = {}
            info_dict_result['title'] = info_dict['title']
            info_dict_result['upload_date'] = info_dict['upload_date']
            info_dict_result['channel'] = info_dict['channel']
            info_dict_result['thumbnails'] = info_dict['thumbnails'][0]['url']
            return result_succ(info_dict_result)
    return result_failure(const.SIMPLE_TASK_FIRST_ERR_GEN_INFO_EMPTY, "TASK_FIRST_ERR_GEN_INFO_EMPTY")


# 添加任务第二步
# 选择：
# 1. 立即执行：只执行一次，单次任务
# 2. 循环执行：按照提供的信息，多次频繁执行
@task_router.route('/simple/second', methods=['POST'])
def task_second():
    result = check_is_login_from_header(request)
    if result != const.GLOBAL_SUCC:
        return result_failure(result, "error in check_is_login_from_header")
    req_json_str = request.data
    req_json = json.loads(req_json_str)
    if not req_json['url']:
        logging.error(f"SIMPLE_TASK_SECOND_URL_EMPTY")
        return result_failure(const.SIMPLE_TASK_SECOND_URL_EMPTY, "SIMPLE_TASK_SECOND_URL_EMPTY")
    token = request.headers.get('token')
    res = db.session.query(FvdOnlineList) \
        .filter(FvdOnlineList.token == token) \
        .first()
    if res:
        user_id = res.user_id if res.user_id else 0
        simple_task = FvdTaskList()
        simple_task.task_url = req_json['url']
        simple_task.task_id = gen_task_id()
        simple_task.user_id = user_id
        simple_task.task_execution_mode = TASK_EXECUTION_EXECUTE_MODE
        simple_task.create_time = datetime.now()
        db.session.add(simple_task)
        db.session.commit()

        g_task_manager.add_simple_task(simple_task)

    return result_succ({})
