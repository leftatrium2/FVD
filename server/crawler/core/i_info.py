from abc import ABCMeta, abstractmethod


class IInfo(metaclass=ABCMeta):
    @abstractmethod
    def info(self, url: str) -> dict:
        pass
