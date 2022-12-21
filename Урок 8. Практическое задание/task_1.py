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
import datetime


class Date:
    day_month_year = '19_12_2022'
    day = 0
    month = 0
    year = 0

    @classmethod
    def date2num(cls):
        cls.day = int(cls.day_month_year.split('_')[0])
        cls.month = int(cls.day_month_year.split('_')[1])
        cls.year = int(cls.day_month_year.split('_')[2])
        return cls.day, cls.month, cls.year

    @staticmethod
    def date_valid(day_month_year):
        day, month, year = map(int, day_month_year.split('_'))
        try:
            datetime.datetime(year, month, day)
        except ValueError:
            print(f'{day_month_year} неверная дата')


print(Date.date2num())
print(Date.day)
print(Date.month)
print(Date.year)
Date.date_valid('19_13_2022')
