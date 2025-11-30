import json
from datetime import datetime

from flask import Blueprint, request
from sqlalchemy import and_

from model.model import IvdUserList, IvdOnlineList
from utils import const
from utils.db import db
from utils.enc_util import md5
from utils.privileges_utils import check_is_admin
from utils.result import result_failure, result_succ

user_router = Blueprint('user', __name__, url_prefix='/user')


@user_router.route('/add', methods=['POST'])
def user_add():
    token = request.headers.get('token')
    ret = check_is_admin(token)
    if ret != const.GLOBAL_SUCC:
        return result_failure(ret, "error")
    req_json_str = request.data
    req_json = json.loads(req_json_str)
    user_name = None
    if 'user_name' in req_json:
        user_name = req_json['user_name'].strip()
    if not user_name or len(user_name) == 0:
        return result_failure(const.LOGIN_ERR_USER_EMPTY, 'LOGIN_ERR_USER_EMPTY')
    password = None
    if 'password' in req_json:
        password = req_json['password'].strip()
    if not password or len(password) == 0:
        return result_failure(const.LOGIN_ERR_USER_OR_PASSWORD_EMPTY, 'LOGIN_ERR_USER_OR_PASSWORD_EMPTY')
    curr_datetime = datetime.now()
    ivd_user_list = IvdUserList()
    ivd_user_list.user_name = user_name
    ivd_user_list.password = md5(password)
    ivd_user_list.create_time = curr_datetime
    db.session.add(ivd_user_list)
    db.session.commit()
    return result_succ({'user_name': user_name})


@user_router.route('/del', methods=['POST'])
def user_del():
    token = request.headers.get('token')
    ret = check_is_admin(token)
    if ret != const.GLOBAL_SUCC:
        return result_failure(ret, "error")
    req_json_str = request.data
    req_json = json.loads(req_json_str)
    user_name = None
    if 'user_name' in req_json:
        user_name = req_json['user_name'].strip()
    if not user_name or len(user_name) == 0:
        return result_failure(const.LOGIN_ERR_USER_EMPTY, 'LOGIN_ERR_USER_EMPTY')
    db.session.query(IvdUserList) \
        .filter(IvdUserList.user_name == user_name) \
        .delete()
    db.session.query(IvdOnlineList) \
        .filter(IvdOnlineList.user_name == user_name) \
        .delete()
    db.session.commit()
    return result_succ({})


@user_router.route('/change_password', methods=['POST'])
def user_change_password():
    token = request.headers.get('token')
    if not token or len(token.strip()) == 0:
        return result_failure(const.LOGIN_ERR_TOKEN_EMPTY, "LOGIN_ERR_TOKEN_EMPTY")
    req_json_str = request.data
    req_json = json.loads(req_json_str)
    old_pass = None
    if 'old_pass' in req_json:
        old_pass = req_json['old_pass'].strip()
    if not old_pass or len(old_pass) == 0:
        return result_failure(const.LOGIN_ERR_OLD_PASS_EMPTY, 'LOGIN_ERR_OLD_PASS_EMPTY')
    new_pass = None
    if 'new_pass' in req_json:
        new_pass = req_json['new_pass'].strip()
    if not new_pass or len(new_pass) == 0:
        return result_failure(const.LOGIN_ERR_NEW_PASS_EMPTY, 'LOGIN_ERR_NEW_PASS_EMPTY')
    if new_pass == old_pass:
        return result_failure(const.LOGIN_ERR_OLD_NEW_PASS_SAME, "LOGIN_ERR_OLD_NEW_PASS_SAME")
    res_list = db.session.query(IvdOnlineList) \
        .filter(IvdOnlineList.token == token) \
        .first()
    if not res_list:
        return result_failure(const.LOGIN_ERR_NOT_LOGIN, 'LOGIN_ERR_NOT_LOGIN')
    user_name = res_list.user_name
    count = db.session.query(IvdUserList) \
        .filter(and_(IvdUserList.user_name == user_name, IvdUserList.password == md5(old_pass))) \
        .count()
    if count != 1:
        return result_failure(const.LOGIN_ERR_OLD_PASS_NOT_MATCH, 'LOGIN_ERR_OLD_PASS_NOT_MATCH')
    db.session.query(IvdUserList) \
        .filter(IvdUserList.user_name == user_name) \
        .update({IvdUserList.password: md5(new_pass)})
    db.session.query(IvdOnlineList) \
        .filter(IvdOnlineList.user_name == user_name) \
        .delete()
    db.session.commit()
    return result_succ({})
