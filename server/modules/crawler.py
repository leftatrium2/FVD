import logging
from datetime import datetime

from flask import Blueprint, request

from crawler import crawler_const
from model.model import FvdCrawlerList
from utils import result, const
from utils.db import db
from utils.task_utils import gen_crawler_hash

crawler_router = Blueprint('crawler', __name__, url_prefix='/crawler')


@crawler_router.route('/register', methods=['GET'])
def crawler_register():
    ip = ''
    if 'ip' in request.args:
        ip = request.args.get('ip')
    rand = ''
    if 'rand' in request.args:
        rand = request.args.get('rand')

    crawler_hash = gen_crawler_hash()
    try:
        crawler_item = FvdCrawlerList()
        crawler_item.crawler_host = ip
        crawler_item.crawler_name = rand
        crawler_item.crawler_hash = crawler_hash
        crawler_item.create_time = datetime.now()
        crawler_item.crawler_status = crawler_const.CRAWLER_STATUS_RUNNING
        db.session.add(crawler_item)
        db.session.commit()
    except Exception as ex:
        logging.error(f"add {ex}")
        return result.result_failure(const.CRAWLER_ERROR_REGISTER, f"CRAWLER_ERROR_REGISTER")

    return result.result_succ({"crawler_hash": crawler_hash})
