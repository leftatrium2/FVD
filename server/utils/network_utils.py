import logging
import os

from cph.utils import constants
from netifaces import interfaces, ifaddresses, AF_INET


def get_current_host() -> str or None:
    """
    获取当前主机ip
    """
    # docker 中获取不到ip传递进去
    if int(os.environ.get('IS_DOCKER', 0)) == 1:
        serverHost = os.environ.get('SERVER_HOST', None)
        logging.info(f"get_current_host by env serverHost:{serverHost}")
        return serverHost
    try:
        loop_back = '127.0.0.1'
        owner_host = ''
        for ifaceName in interfaces():
            address = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': ''}])][0]
            if address is not None and address.strip() != '':
                if address.strip() != loop_back:
                    owner_host = address
    except Exception as ex:
        from app import get_info_log
        get_info_log().log(constants.INFOLOG_MODULE_COMMON_KEY, constants.GLOBAL_ERROR_GET_CURRENT_HOST, str(ex))
        logging.error(ex)
        return None
    logging.info(f"get_current_host owner_host:{owner_host}")
    return owner_host
