from abc import ABC, abstractmethod


class AbstractHeadHunterAPI(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def get_params(self):
        pass

    @abstractmethod
    def input_set(self):
        pass

    @property
    @abstractmethod
    def requests_get(self):
        pass
