import yt_dlp

from crawler.core.i_info import IInfo


class YTDlpInfo(IInfo):
    def info(self, url: str) -> dict:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'forcejson': True,
            'noprogress': True,
            'simulate': True,
            "skip_download": True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            data = ydl.extract_info(url, download=False, process=False)

        return data
