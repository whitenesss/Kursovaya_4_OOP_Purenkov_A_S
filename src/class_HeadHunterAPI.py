# -*- coding: utf-8 -*-
import requests
from src.class_abstractn import AbstractHeadHunterAPI


class HeadHunterAPI(AbstractHeadHunterAPI):
    '''Формируем зарос из юрл, парвметров и выводим запрос'''

    def __init__(self, url, params):
        self.url = url
        self.params = params

    @property
    def requests_get(self):
        return requests.get(self.url, params=self.params)


if __name__ == '__main__':
    pass
