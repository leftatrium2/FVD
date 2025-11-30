from crawler.core.i_context import IContext
from crawler.core.i_downloader import IDownloader


class KuaishouDownloader(IDownloader):
    def download(self, url: str, ctx: IContext) -> dict:
        pass
