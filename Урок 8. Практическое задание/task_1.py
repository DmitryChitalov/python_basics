"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут
day_month_year, присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной
структуры на реальных данных.
"""


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'All right'
                else:
                    return f'Incorrect Year'
            else:
                return f'Incorrect Month'
        else:
            return f'Incorrect Day'

    def __str__(self):
        return f'Current date {Data.extract(self.day_month_year)}'


today = Data('09 - 11 - 2022')
print(today)
print(Data.valid(7, 2, 2022))
print(Data.valid(11, 7, 2014))
print(Data.valid(11, 5, 2022))
print(Data.valid(18, 5, 2019))
print(today.valid(11, 13, 2011))
print(Data.valid(1, 11, 2000))