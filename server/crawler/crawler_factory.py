import sys

from crawler.core.i_downloader import IDownloader
from crawler.core.i_info import IInfo
from crawler.impl.yt_dlp.yt_dlp_downloader import YTDlpDownloader
from crawler.impl.yt_dlp.yt_dlp_info import YTDlpInfo
from crawler.utils.crawler_const import SPECIAL_INFO_DOMAIN, SPECIAL_DOWNLOADER_DOMAIN
from crawler.utils.url_utils import get_domain
from crawler.utils.yt_dlp_utils import ytdlp_support_manager


class CrawlerFactory(object):
    def gen_info(self, url: str) -> IInfo or None:
        if not url:
            return None
        domain = get_domain(url)
        for key, value in SPECIAL_INFO_DOMAIN.items():
            if key == domain:
                return value()
        if ytdlp_support_manager.is_support_site(domain):
            return YTDlpInfo()
        return None

    def gen_downloader(self, url: str) -> IDownloader or None:
        if not url:
            return None
        domain = url
        for key, value in SPECIAL_DOWNLOADER_DOMAIN.items():
            if key == domain:
                return value()
        if ytdlp_support_manager.is_support_site(domain):
            return YTDlpDownloader()
        return None


crawler = CrawlerFactory()

if __name__ == "__main__":
    info = crawler.gen_info("https://www.youtube.com/watch?v=n5sZJhAyFR0")
    if not info:
        print("failure")
        sys.exit(-1)
    info.info("https://www.youtube.com/watch?v=n5sZJhAyFR0")
    pass
