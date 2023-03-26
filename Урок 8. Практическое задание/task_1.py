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


class Date:
    day_month_year = ''
    day = 0
    month = 0
    year = 0

    @classmethod
    def set_day_month_year(cls, day_month_year):
        Date.day_month_year = day_month_year
        if len(Date.day_month_year) == 8:
            Date.day = int(Date.day_month_year[0:2])
            Date.month = int(Date.day_month_year[2:4])
            Date.year = int(Date.day_month_year[4:8])

    @staticmethod
    def validate():
        if (Date.year < 1900):
            print('Год не может быть меньше 1900')
        elif (Date.month < 1 or Date.month > 12):
            print('Месяц должен быть в диапазоне от 1 до 12')
        elif (Date.day < 1 or Date.day > 31):
            print('День должен быть в диапазоне от 1 до 31')
        else:
            print(f'{Date.day_month_year} - корректна')

Date.set_day_month_year('04052020')
print(Date.day_month_year)
print(Date.day, Date.month, Date.year)
Date.validate()
