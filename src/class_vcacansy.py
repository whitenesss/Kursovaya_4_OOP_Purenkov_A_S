
class Vacancy:
    '''
    класс для взаимодействия в вакансиями
    '''
    def __init__(self, name, url, city, salary_from, salary_to, currency, requirements):
        self.name = name
        self.url = url
        self.city = city
        if salary_from:
            self.salary_from = salary_from
        else:
            self.salary_from = 0
        if salary_to:
            self.salary_to = salary_to
        else:
            self.salary_to = 0
        self.currency = currency
        self.requirements = requirements

    def __str__(self):
        '''
        красивый вывод в кансоль при надобнасти
        :return:
        '''
        if self.salary_from == 0 and self.salary_to == 0 and self.currency is None:
            return (f"Название вакансии: {self.name}\n"
                    f"Ссылка: {self.url}\n"
                    f"Город: {self.city}\n"  # Добавлен пробел после двоеточия
                    f"Зарплата: зарплата не указана\n"
                    f"Требования: {self.requirements}"
                    f"\n---")
        else:
            return (f"Название вакансии: {self.name}\n"
                    f"Ссылка: {self.url}\n"
                    f"Город: {self.city}\n"  # Добавлен пробел после двоеточия
                    f"Зарплата: {self.salary_from}-{self.salary_to} {self.currency}.\n"
                    f"Требования: {self.requirements}"
                    f"\n---")

    # Методы сравнения вакансий по зарплате между собой

    def __eq__(self, other: object) -> bool:
        """
        метод проверяет
        равны ли два объекта

        :param other: (object) объект класса с которым сравнивать
        :return: (bool) True | False
        """
        return self.salary_from == other.salary_from

    def __lt__(self, other):
        """
        метод проверяет
        какой из объектов больше

        :param other: (object) объект класса с которым сравнивать
        :return: (bool) True | False
        """
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        """
        метод проверяет
        какой из объектов меньше

        :param other: (object) объект класса с которым сравнивать
        :return: (bool) True | False
        """
        return self.salary_from > other.salary_from

    @classmethod
    def cast_to_object_list(cls, vacancies_data: dict):
        '''
        создаем экземпляр клас Vacansy c учетом отсутствия selary
        :param vacancies_data:
        :return:
        '''
        vacancy_objects = []
        for vacancy_data in vacancies_data:
            city = vacancy_data.get('area', {}).get('name')

            if vacancy_data.get('salary') is not None:
                salary_from = vacancy_data.get('salary', {}).get('from')
                if salary_from is None:
                    salary_from = 0
                salary_to = vacancy_data.get('salary', {}).get('to')
                if salary_to is None:
                    salary_to = 0
                currency = vacancy_data.get('salary', {}).get('currency')

            else:
                salary_from = 0
                salary_to = 0
                currency = ''
            vacancy = cls(
                name=vacancy_data.get('name'),
                url=vacancy_data.get('alternate_url'),
                city=city,
                salary_from=salary_from,
                salary_to=salary_to,
                currency=currency,
                requirements=vacancy_data.get('experience').get('name')
            )
            vacancy_objects.append(vacancy)
        return vacancy_objects
