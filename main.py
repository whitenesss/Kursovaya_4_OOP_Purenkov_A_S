from src.class_record import JsonStorage
from src.class_HeadHunterAPI import HeadHunterAPI
from src.class_vcacansy import Vacancy
from src.fanc import filter_vacancies, get_vacancies_by_salary, get_top_vacancies, sort_vacancies

# Создание экземпляра класса для работы с API сайтов с вакансиями
def user_interaction():

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.requests_get
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    print(f"Получено {len(vacancies_list)} вакансий с HeadHunter")
    # Загрузка данных из JSON файла
    vacancies_data = JsonStorage.load_json()

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    print("Введите диапазон зарплат")
    salary_range = input("Пример ввода: 100000 - 150000 :  ")  # Пример: 100000 - 150000
    # Применение фильтрации и сортировки к вакансиям
    print(type(vacancies_data))
    filtered_vacancies = filter_vacancies(vacancies_data, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)

    # Получение топ N вакансий
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    # Вывод результатов в консоль

    for i, vacancy in enumerate(top_vacancies, start=1):
        try:
            print(f"{i}. Название вакансии: {vacancy['name']}")
        except UnicodeEncodeError:
            print(f"{i}. Название вакансии: {vacancy['name'].encode('utf-8')}")


if __name__ == '__main__':
    print("Запуск программы...")
    user_interaction()
    print("Программа завершена.")