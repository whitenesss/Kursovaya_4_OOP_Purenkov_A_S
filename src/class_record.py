import logging
import json


class JsonStorage:
    @staticmethod
    def creating_json(vacancies: list):
        """
        Функция принимает список объектов класса Vacancy и записывает их в формате JSON.

        :param vacancies: (list[Vacancy]) Список объектов класса Vacancy.
        """
        list_vacancies = []
        for vacancy in vacancies:
            if vacancy.salary_from == 0 and vacancy.salary_to == 0 and vacancy.currency is None:
                vacancies_data = {
                    "name": vacancy.name,
                    "city": vacancy.city,
                    "salary": "Зарплата не указана...",
                    "requirement": vacancy.requirements,
                    "url": vacancy.url
                }
                list_vacancies.append(vacancies_data)
            else:
                vacancies_data = {
                    "name": vacancy.name,
                    "city": vacancy.city,
                    "salary_from": vacancy.salary_from,
                    "salary_to": vacancy.salary_to,
                    "currency": vacancy.currency,
                    "requirement": vacancy.requirements,
                    "url": vacancy.url
                }
                list_vacancies.append(vacancies_data)

        with open('data/hh.json', "w") as file:
            json.dump(list_vacancies, file, ensure_ascii=False, indent=4)

    @staticmethod
    def load_json():
        """
        Загрузка данных из JSON-файла.
        """
        with open('data/hh.json', 'r', encoding='utf-8', errors='replace') as file:
            return json.load(file)

    @staticmethod
    def delete_vacancy(vacancy_name: str):
        """
        Удаление вакансии по названию.
        """
        with open('data/hh.json', 'r+', encoding='utf-8') as file:
            data = json.load(file)
            # Проверяем наличие вакансии с указанным названием
            found_vacancies = [v for v in data if v.get('name') == vacancy_name]
            if found_vacancies:
                data = [v for v in data if v['name'] != vacancy_name]
                file.seek(0)
                json.dump(data, file, ensure_ascii=False, indent=4)
                logging.info(f"Vacancy with name '{vacancy_name}' deleted successfully.")
            else:
                logging.warning(f"Vacancy with name '{vacancy_name}' not found.")


if __name__ == '__main__':
    pass
