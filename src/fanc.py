def filter_vacancies(vacancies_data: list, filter_words: str):
    """
    поис вакансии из json по пораметрам пользователя
    :param vacancies_data: берем данные из файла json
    :param filter_words: рапрашиваем слово ключевое у пользоватеоля
    :return:
    """

    filtered_vacancies = []
    for vacancy in vacancies_data:
        for word in filter_words:
            if word.lower() in vacancy['name'].lower():
                filtered_vacancies.append(vacancy)
                break  # Прерываем внутренний цикл, чтобы не добавлять вакансию несколько раз
    return filtered_vacancies


def get_vacancies_by_salary(vacancies_data: list, salary_range: str):
    """
     Эта функция выбирает вакансии из списка (vacancies_data),
     удовлетворяющие заданному диапазону зарплат (salary_range).
     Диапазон зарплат задается в формате "минимальная_зарплата-максимальная_зарплата".
     Функция преобразует строку salary_range в два числа: min_salary (минимальная зарплата) и max_salary (максимальная зарплата).
     Затем она проходит по каждой вакансии в списке и добавляет вакансию в список ranged_vacancies, если её зарплата находится в заданном диапазоне.
     Функция возвращает список вакансий, отфильтрованных по зарплате.
    :param vacancies_data: json file
    :param salary_range: ввод пользователя
    :return:
    """
    min_salary, max_salary = map(int, salary_range.split('-'))
    ranged_vacancies = []
    for vacancy in vacancies_data:
        if vacancy['salary_from'] >= min_salary and vacancy['salary_to'] <= max_salary:
            ranged_vacancies.append(vacancy)
    return ranged_vacancies


def sort_vacancies(vacancies_data: list):
    """
    Эта функция сортирует список вакансий (vacancies_data) по убыванию зарплаты
    :param vacancies_data:
    :return:
    """
    return sorted(vacancies_data, key=lambda x: x.get('salary_from', 0), reverse=True)


def get_top_vacancies(vacancies_data: list, top_n):
    """
     Она просто возвращает первые N вакансий из списка.
    :param vacancies_data:
    :param top_n:
    :return:
    """
    return vacancies_data[:top_n]


def serch_query():
    """функция поискового запроса"""
    search_query = input("Введите поисковый запрос: ")
    return search_query


def serch_area():
    """функция для hh исключительно для выбора города"""
    print('Москва, Санкт-Питербург, Краснодар')
    search_area = input("выберете город: ")
    counter = 0
    while counter == 0:
        if search_area.lower() == 'москва':
            search_area = 1
            counter += 1
            return search_area
        elif search_area.lower() == 'санкт-питербург':
            search_area = 2
            counter += 1
            return search_area
        elif search_area.lower() == 'краснодар':
            search_area = 53
            counter += 1
            return search_area
        else:
            print('ввели не верно')
            search_area = input("выберете город: ")
