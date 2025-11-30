import os
from os import getcwd


class YTDlpSupportManager(object):
    _support_site_keyword = []

    def init(self):
        curr_path = os.getcwd() + os.sep + "crawler" + os.sep + "utils" + os.sep + "support.config"
        fp = open(curr_path)
        self._support_site_keyword = fp.read().splitlines()

    def is_support_site(self, site: str) -> bool:
        if self._support_site_keyword:
            for keyword in self._support_site_keyword:
                if keyword in site:
                    return True
        return False


ytdlp_support_manager = YTDlpSupportManager()

if __name__ == "__main__":
    ytdlp_support_manager.init()
    if ytdlp_support_manager.is_support_site("https://www.youtube.com/watch?v=1BRebNUbqaI"):
        print("OK")
