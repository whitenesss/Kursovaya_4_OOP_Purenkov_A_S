# -*- coding: utf-8 -*-
import requests
import logging
from src.class_abstractn import AbstractHeadHunterAPI


class HeadHunterAPI(AbstractHeadHunterAPI):
    '''Формируем зарос из юрл, параметров и выводим запрос'''
    order_by = "relevance"

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.order_by = 'relevance'

    def get_params(self, keyword: str, area: str):
        '''
        подготовка параметров для запроса
        :param keyword: основной параметр поиска
        :param area: город
        :return: словарь параметров
        '''
        params = {
            'text': keyword,
            'area': area,
            'per_page': 100,
            'order_by': self.order_by,
            # 'only_with_salary': True

        }
        return params

    def input_set(self):
        '''
        Возможность получения вакансий с хх с дополнительной фильтрацией
        :return:
        '''
        filtr = {'Сортировка по релевантности': 'relevance',
                 'Сортировка по убыванию заработной платы': 'salary_desc',
                 'Сортировка по возрастанию заработной платы': 'salary_asc'}
        print('выбирете фильтрацию')
        print(f'{", ".join(f"{k}" for k in filtr.keys())}')

        user_input = input('введите фильтрацию: ').capitalize()
        count = 0
        while count == 0:
            if user_input in filtr.keys():
                self.order_by = filtr[user_input]
                count += 1
            else:
                print('даннык введены не коректоно')
                user_input = input('введите фильтрацию снова: ').capitalize()

    @property
    def requests_get(self):
        '''
        Собираем порамитры для запроса апи к hh и выдаем готовый к обработке запрос
        '''
        search_query = input("Введите поисковый запрос: ")
        print('Москва, Санкт-Питербург, Краснодар')
        search_area = input("выберете город: ")
        counter = 0
        while counter == 0:
            if search_area.lower() == 'москва':
                search_area = 1
                counter += 1
            elif search_area.lower() == 'санкт-питербург':
                search_area = 2
                counter += 1
            elif search_area.lower() == 'краснодар':
                search_area = 53
                counter += 1
            else:
                print('ввели не верно')
                search_area = input("выберете город: ")
        params = self.get_params(search_query, search_area)
        try:
            response = requests.get(self.__url, params=params)
            response.raise_for_status()  # Проверяем статус ответа
            if response.status_code == 200:
                return response.json()['items']
            else:
                logging.error(f"Failed to fetch data from API. Status code: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            logging.error(f"Error occurred while fetching data from API: {e}")
            return None


if __name__ == '__main__':
    pass
