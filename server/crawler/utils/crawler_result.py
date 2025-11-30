from crawler.utils import crawler_const


def crawler_result_succ(data: dict) -> dict:
    return {
        "code": crawler_const.GLOBAL_ERR_SUCC,
        "msg": 'succ',
        "data": data
    }


def crawler_result_failure(code: int, msg: str) -> dict:
    return {
        "code": code,
        "msg": msg,
        "data": {}
    }
