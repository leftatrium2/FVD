from urllib import parse


def get_domain(url: str) -> str or None:
    parse_dict = parse.urlparse(url)
    return parse_dict.netloc.strip().replace("www.", "")
