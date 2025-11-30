from abc import ABCMeta, abstractmethod

from crawler.core.i_context import IContext


class IDownloader(metaclass=ABCMeta):
    @abstractmethod
    def download(self, url: str, ctx: IContext) -> dict:
        pass
