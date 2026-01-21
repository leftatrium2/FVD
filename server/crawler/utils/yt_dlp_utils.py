import os
from os import getcwd


class YTDlpSupportManager(object):
    _support_site_keyword = []

    def __init__(self):
        curr_path = os.getcwd() + os.sep + "crawler" + os.sep + "utils" + os.sep + "support.config"
        fp = open(curr_path)
        self._support_site_keyword = fp.read().splitlines()

    def is_support_site(self, domain: str) -> bool:
        if self._support_site_keyword:
            for keyword in self._support_site_keyword:
                if domain.lower() in keyword.lower():
                    return True
        return False


ytdlp_support_manager = YTDlpSupportManager()

if __name__ == "__main__":
    if ytdlp_support_manager.is_support_site("youtube.com"):
        print("OK")
