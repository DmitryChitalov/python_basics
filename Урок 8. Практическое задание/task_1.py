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
    day_month_year = '01.01.2022'

    @classmethod
    def date_to_int(cls):
        dmy = Date.day_month_year.split('.')
        cls.day = int(dmy[0])
        cls.month = int(dmy[1])
        cls.year = int(dmy[2])
        print(f'Число - {cls.day}, месяц - {cls.month}, год - {cls.year}')

    @staticmethod
    def date_validation():
        dmy = Date.day_month_year.split('.')
        if 0 < int(dmy[0]) <= 31 and 1 <= int(dmy[1]) <= 12 and 0 < int(
                dmy[2]):
            return 'Дата введена корректно.'
        return 'Указана некорректная дата!'


a = Date()
a.date_to_int()
Date.date_to_int()
print(Date.day_month_year)
print(a.date_validation())
Date.day_month_year = '-1.02.1998'
print(Date.day_month_year)
print(a.date_validation())
Date.date_to_int()
