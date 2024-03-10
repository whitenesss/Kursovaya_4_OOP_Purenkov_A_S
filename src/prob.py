import json
import requests
import os

url_2 ='https://api.hh.ru/suggests/vacancy_search_keyword'
url = "https://api.hh.ru/vacancies"
params = {
    "text": "Python junior",
    "area": 1,  # Москва
    "salary": "150000",
    "experience": "between3And6",
    "employment": "full",
    "schedule": "remote",
    "order_by": "relevance",
    "per_page": 2,  # Количество результатов на страницу
    "page": 0  # Номер страницы
}

response_2 = requests.get(url_2, params=params)
response = requests.get(url, params=params)
# print(response.status_code)
# print(response.json())
vacancies = response.json()


print(response_2.json())
for vacancy in vacancies.get("items", []):
    print(vacancy["name"], vacancy["salary"], vacancy["employer"]["name"])

with open('../data/hh.json', 'w', encoding='utf=8') as file:
    json.dump(response.json(), file, ensure_ascii=False, indent=4)
