# -*- coding: utf-8 -*-
import sqlite3
import json


class Record:
    """класс записи данных в файл"""

    def __init__(self, value_json):
        self.value_json = value_json
        self.connect = None
        self.cursor = None

    def creating_table(self, name):
        """'''создание таблици'''"""
        self.connect = sqlite3.connect(name)
        self.cursor = self.connect.cursor()
        self.cursor.execute('DROP TABLE IF EXISTS vacancies')
        self.cursor.execute('''
        CREATE TABLE vacancies (
            name TEXT,
            area_name TEXT,
            salary_from INTEGER,
            salary_to INTEGER,
            salary_currency TEXT,
            employer_name TEXT,
            published_at TEXT,
            experience_name TEXT,
            employment_name TEXT
        )
    ''')

    def adding_table(self):
        """'''добавление в таблицу'''"""
        for data_sql in self.value_json.get("items", []):
            salary_info = data_sql.get('salary', {})
            if salary_info is not None:
                salary_from = salary_info.get('from')
            else:
                salary_from = 0
            salary_info_to = data_sql.get('salary', {})
            if salary_info_to is not None:
                salary_to = salary_info_to.get('to')
            else:
                salary_to = 0
            salary_info = data_sql.get('salary', {})
            if salary_info is not None:
                salary_currency = salary_info.get('currency')
            else:
                salary_currency = None
            data = {'name': data_sql.get('name').encode('utf-8', 'ignore').decode('utf-8'),
                    'area_name': data_sql.get('area', {}).get('name').encode('utf-8', 'ignore').decode('utf-8'),
                    'salary_from': salary_from,
                    'salary_to': salary_to,
                    'salary_currency': salary_currency,
                    'employer_name': data_sql.get('employer', {}).get('name').encode('utf-8', 'ignore').decode(
                        'utf-8'),
                    'published_at': data_sql.get('published_at').encode('utf-8', 'ignore').decode('utf-8'),
                    'experience_name': data_sql.get('experience', {}).get('name').encode('utf-8', 'ignore').decode(
                        'utf-8'),
                    'employment_name': data_sql.get('employment', {}).get('name').encode('utf-8', 'ignore').decode(
                        'utf-8')
                    }

            self.cursor.execute('''
                INSERT INTO vacancies (name, area_name, salary_from, salary_to, salary_currency, employer_name, published_at, experience_name, employment_name)
                VALUES (:name, :area_name, :salary_from, :salary_to, :salary_currency, :employer_name, :published_at, :experience_name, :employment_name)
            ''', data)
            self.connect.commit()
        self.connect.close()

    def creating_json(self):
        """'''заристь в json файл'''"""
        with open('data/hh.json', 'w', encoding='utf=8') as file:
            json.dump(self.value_json, file, ensure_ascii=False, indent=4)


if __name__ in '__main__':
    pass
