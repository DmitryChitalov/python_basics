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
from datetime import datetime


class Date:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def my_classmethod(cls, day_month_year):
        my_date = list(map(int, day_month_year.split("-")))
        return my_date

    @staticmethod
    def my_valid(day_month_year):
        try:
            my_check = datetime.strptime(day_month_year, '%d-%m-%Y')
            print(my_check)
            return "Done"
        except ValueError:
            return "bad date"


d1 = "21-12-2022"
print(Date.my_classmethod(d1))
print(Date.my_valid(d1))
d2 = "333-3333-3321"
print(Date.my_valid(d2))
