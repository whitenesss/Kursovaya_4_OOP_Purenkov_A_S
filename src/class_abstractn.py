from abc import ABC, abstractmethod


class AbstractHeadHunterAPI(ABC):
    @abstractmethod
    def __init__(self, url, params):
        self.url = url
        self.params = params

    @property
    @abstractmethod
    def requests_get(self):
        pass
