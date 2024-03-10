# -*- coding: utf-8 -*-
from src.class_serch_param import SearchParam
from src.class_HeadHunterAPI import HeadHunterAPI
from src.class_record import Record
from prettytable import PrettyTable
import sqlite3


def user_interaction():
    """получаеи от пользователя данные для записи в таблицу"""
    platforms = 'https://api.hh.ru/vacancies'
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
    alary_range = input("Введите желаемую зарплату: ")

    search_param = SearchParam(search_query, search_area, alary_range)
    search_param.inpust_set()
    respons = HeadHunterAPI(platforms, search_param.get())
    record = Record(respons.requests_get.json())
    record.creating_table('data/privet.db')
    record.adding_table()
    record.creating_json()


def printing():
    """выводим запрашиваемые данные из сформированого файла"""
    conn = sqlite3.connect('data/privet.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vacancies")
    rows = cursor.fetchall()
    table = PrettyTable()
    table.field_names = [description[0] for description in cursor.description]
    for row in rows:
        table.add_row(row)
    print(table)


if __name__ in '__main__':
    user_interaction()
    printing()
