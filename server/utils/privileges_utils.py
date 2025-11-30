from datetime import datetime

from model.model import FvdOnlineList, FvdUserList
from utils import const
from utils.db import db


def check_is_admin(token: str) -> int:
    if not token:
        return const.LOGIN_ERR_TOKEN_EMPTY
    res_list = db.session.query(FvdOnlineList) \
        .filter(FvdOnlineList.token == token)
    if len(res_list) != 1:
        return const.LOGIN_ERR_NOT_LOGIN
    user_name = res_list[0].user_name
    res_list = db.session.query(FvdUserList) \
        .filter(FvdUserList.user_name == user_name)
    if len(res_list) != 1:
        return const.LOGIN_ERR_USER_OR_PASSWORD
    privilege = int(res_list[0].privilege)
    if privilege == 0:
        return const.GLOBAL_SUCC
    return const.LOGIN_ERR_USER_NOT_ADMIN


def check_is_login_from_header(request) -> int:
    token = request.headers.get('token')
    if not token:
        return const.LOGIN_ERR_TOKEN_EMPTY
    return check_is_login(token)


def check_is_login(token: str) -> int:
    res = db.session.query(FvdOnlineList) \
        .filter(FvdOnlineList.token == token) \
        .first()
    if res:
        valid_time = res.valid_time
        curr_time = datetime.now()
        if curr_time >= valid_time:
            db.session.query(FvdOnlineList) \
                .filter(FvdOnlineList.token == token) \
                .delete()
            db.session.commit()
            return const.LOGIN_ERR_TOKEN_TIMEOUT
        return const.GLOBAL_SUCC
    return const.LOGIN_ERR_TOKEN_INVALID
