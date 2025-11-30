from abc import ABCMeta, abstractmethod


class IContext(metaclass=ABCMeta):
    @abstractmethod
    def on_create(self, url: str):
        pass

    @abstractmethod
    def on_start(self, url: str):
        pass

    @abstractmethod
    def on_progress(self, url: str, progress: float):
        pass

    @abstractmethod
    def on_finish(self, url: str, code: int, msg: str):
        pass
