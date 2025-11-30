import json

import requests
from flask import Blueprint

from model.model import FvdToken
from utils import global_var, const, menu
from utils.db import db
from utils.result import result_succ

menu_router = Blueprint("menu", __name__, url_prefix="/menu")


@menu_router.route("/", methods=["GET"])
def menu_index():
    res = db.session.query(FvdToken) \
        .first()
    auth_url = global_var.get_value(const.AUTH_URL_KEY)
    if res.token and len(res.token.strip()) > 0:
        token = res.token
        response = requests.get(f"{auth_url}/auth?token={token}")
        if response.status_code == 200:
            resp_json = json.loads(response.text)
            if resp_json and resp_json['code'] == 0:
                return result_succ(menu.PROFESSIONAL_MENU_CONFIG)
    return result_succ(menu.BASIC_MENU_CONFIG)
