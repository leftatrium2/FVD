from crawler.impl.douyin.douyin_downloader import DouyinDownloader
from crawler.impl.douyin.douyin_info import DouyinInfo
from crawler.impl.kuaishou.kuaishou_downloader import KuaishouDownloader
from crawler.impl.kuaishou.kuaishou_info import KuaishouInfo
from crawler.impl.xiaohongshu.xiaohongshu_downloader import XHSDownloader
from crawler.impl.xiaohongshu.xiaohongshu_info import XHSInfo

SPECIAL_INFO_DOMAIN = {
    'douyin.com': DouyinInfo,
    'kuaishou.com': KuaishouInfo,
    'xiaohongshu.com': XHSInfo
}
SPECIAL_DOWNLOADER_DOMAIN = {
    'douyin.com': DouyinDownloader,
    'kuaishou.com': KuaishouDownloader,
    'xiaohongshu.com': XHSDownloader
}
# error code for crawler
GLOBAL_ERR_SUCC = 0
GLOBAL_ERR_UNKNOWN = 1000
GLOBAL_ERR_HAS_NOT_CONTEXT = 1002
# error code for yt-dlp
# error code for others
