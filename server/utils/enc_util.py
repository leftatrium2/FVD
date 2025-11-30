import hashlib


def md5(src: str) -> str:
    hl = hashlib.md5()
    hl.update(src.encode(encoding='utf-8'))
    return hl.hexdigest()
