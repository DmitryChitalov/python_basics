"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

class Data:
    def __init__(self, day_month_year):
        # self.day = day
        # self.month = month
        # self.year = year
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_dt = []

        for i in day_month_year.split():
            if i != '-': my_dt.append(i)

        return int(my_dt[0]), int(my_dt[1]), int(my_dt[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Корректно'
                else:
                    return f'Некорректный год'
            else:
                return f'Некорректный месяц'
        else:
            return f'Некорректный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('12 - 2 - 2023')
print(today)
print(Data.valid(11, 11, 2023))
print(today.valid(10, 15, 2022))
print(Data.extract('11 - 11 - 2022'))
print(today.extract('11 - 11 - 2020'))
print(Data.valid(1, 12, 2010))