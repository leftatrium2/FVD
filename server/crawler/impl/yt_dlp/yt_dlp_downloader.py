from crawler.core.i_context import IContext
from crawler.core.i_downloader import IDownloader
from crawler.utils import crawler_result, crawler_const


class YTDlpDownloader(IDownloader):
    def download(self, url: str, ctx: IContext) -> dict:
        if not ctx:
            return crawler_result.crawler_result_failure(code=crawler_const.GLOBAL_ERR_HAS_NOT_CONTEXT,
                                                         msg="GLOBAL_ERR_HAS_NOT_CONTEXT")
        ctx.on_create(url)
        return crawler_result.crawler_result_succ({})
