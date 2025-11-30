import uuid


def gen_task_id() -> str:
    uuid_str = str(uuid.uuid1())
    uuid_str = uuid_str.replace('-', '')
    return uuid_str


def gen_crawler_hash() -> str:
    uuid_str = str(uuid.uuid1())
    uuid_str = uuid_str.replace('-', '')
    return uuid_str
