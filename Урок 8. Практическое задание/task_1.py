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


class MyData:
    day = None
    month = None
    year = None

    day_month_year = '11.03.2023'

    def __init__(self, day, month, year):
        MyData.day_month_year = day + '.' + month + '.' + year

    # def __str__(self):
    #     return f"{day_month_year}"
    @classmethod
    def dispatch(cls, hash_):
        cls.day = int(hash_[:2])
        cls.month = int(hash_[2:4])
        cls.year = int(hash_[4:])
        return cls(hash_[:2], hash_[2:4], hash_[4:])

    @staticmethod
    def check_date(day, month, year):
        isValidDate = True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False

        if isValidDate:
            print("Дата верна ...")
        else:
            print("Дата не верна ...")

    @classmethod
    def get_data(cls):
        return f"{cls.day_month_year}"


print(MyData.dispatch("22111980").get_data())
print(MyData.get_data())
print(MyData.year)
MyData.check_date(23, 99, 2012)
