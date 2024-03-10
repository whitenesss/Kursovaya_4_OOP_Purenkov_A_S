class SearchParam:
    '''класс формирования параметров поиска '''
    order_by = "relevance"

    def __init__(self, text, area, salary):
        self.text = text
        self.area = area
        self.salary = salary
        self.per_page = 30
        self.order_by = "relevance"

    def get(self):
        return self.__dict__

    def inpust_set(self):

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


if __name__ == '__main__':
    pass
