import json
from datetime import datetime, timedelta

from flask import Blueprint, request
from sqlalchemy import and_

from model.model import FvdUserList, FvdOnlineList
from utils import const
from utils.db import db
from utils.enc_util import md5
from utils.result import result_failure, result_succ
from utils.privileges_utils import check_is_login

login_router = Blueprint('login', __name__, url_prefix='/login')


@login_router.route('/', methods=['POST'])
def login():
    req_json_str = request.data
    req_json = json.loads(req_json_str)
    user_name = None
    password = None
    if 'username' in req_json:
        user_name = req_json['username']
    if 'password' in req_json:
        password = req_json['password']
    if not user_name or not password:
        return result_failure(const.LOGIN_ERR_USER_OR_PASSWORD_EMPTY, 'LOGIN_ERR_USER_OR_PASSWORD_EMPTY')
    count = db.session.query(FvdUserList) \
        .filter(and_(FvdUserList.user_name == user_name, FvdUserList.password == md5(password))) \
        .count()
    if count <= 0:
        return result_failure(const.LOGIN_ERR_USER_OR_PASSWORD, "LOGIN_ERR_USER_OR_PASSWORD")
    res = db.session.query(FvdOnlineList.user_name,
                           FvdOnlineList.valid_time,
                           FvdOnlineList.token,
                           FvdUserList.avatar,
                           FvdUserList.nickname,
                           FvdUserList.roles,
                           FvdUserList.permissions) \
        .select_from(FvdOnlineList) \
        .join(FvdUserList, FvdUserList.user_name == FvdOnlineList.user_name) \
        .filter(FvdOnlineList.user_name == user_name) \
        .first()
    if not res:
        curr_datetime = datetime.now()
        valid_datetime = curr_datetime + timedelta(days=3 * 30)
        token = md5(str(curr_datetime))
        curr_user_list = FvdOnlineList()
        curr_user_list.user_name = user_name
        curr_user_list.token = token
        curr_user_list.create_time = curr_datetime
        curr_user_list.valid_time = valid_datetime
        db.session.add(curr_user_list)
        db.session.commit()
        res = db.session.query(FvdOnlineList.user_name,
                               FvdOnlineList.valid_time,
                               FvdOnlineList.token,
                               FvdUserList.avatar,
                               FvdUserList.nickname,
                               FvdUserList.roles,
                               FvdUserList.permissions) \
            .select_from(FvdOnlineList) \
            .join(FvdUserList, FvdUserList.user_name == FvdOnlineList.user_name) \
            .filter(FvdOnlineList.user_name == user_name) \
            .first()
    if res:
        return result_succ({
            'token': res.token,
            'avatar': res.avatar,
            'username': res.user_name,
            'nickname': res.nickname,
            'roles': res.roles,
            'permissions': res.permissions,
            'expires': res.valid_time
        })
    return result_failure(const.LOGIN_ERR_TOKEN_REFRESH, "LOGIN_ERR_TOKEN_REFRESH")


@login_router.route('/logout', methods=['GET'])
def logout():
    token = request.headers.get('token')
    if not token:
        return result_failure(const.LOGIN_ERR_TOKEN_EMPTY, "LOGIN_ERR_TOKEN_EMPTY")
    db.session.query(FvdOnlineList) \
        .filter(FvdOnlineList.token == token) \
        .delete()
    db.session.commit()
    return result_succ({})


# 检查Token是否可用
@login_router.route('/token', methods=['GET'])
def token():
    curr_token = request.headers.get('token')
    if not curr_token:
        return result_failure(const.LOGIN_ERR_TOKEN_EMPTY, "LOGIN_ERR_TOKEN_EMPTY")

    result = check_is_login(curr_token)
    if (result == const.GLOBAL_SUCC):
        return result_succ({})
    return result_failure(result, "${check_is_login}")
