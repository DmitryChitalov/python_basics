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

class MyDate:

    def __init__(self, date):
        self.date = date.split("-")

    @classmethod
    def dmy(cls, date):
        try:
            d, m, y = [int(el) for el in date.split("-")]
            return f"Типы объектов число: {type(d), d}, {type(m), m},{type(y), y}"
        except ValueError:
            return "Дата введена не верно!"

    @staticmethod
    def validate(date):
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return "Всё ок!"
        except ValueError:
            return "Не верно введена дата!"


print(MyDate.dmy("22-11-21"))
print(MyDate.validate("2021-12-31"))
print(MyDate.validate("2021-13-31"))