# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, day_month_year):
        # self.day = day
        # self.month = month
        # self.year = year
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return print(f'день {int(my_date[0])}, месяц {int(my_date[1])}, год {int(my_date[2])}')

    @staticmethod
    def valid(day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        if 1 <= int(my_date[0]) <= 31:
            if 1 <= int(my_date[1]) <= 12:
                if 3000 >= int(my_date[2]) >= 0:
                    return f'все ок'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


print(Data.valid('04 - 11 - 2022'))
print("____")
print(Data.extract('04 - 11 - 2011'))
print("____")
print(Data.valid('04 - 15 - 2000'))
print("____")
