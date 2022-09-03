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
class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.d = day
        self.m = month
        self.y = year

    @classmethod
    def conver(cls, date_str):
        day, month, year = map(int, date_str.split("-"))
        numm = cls(day, month, year)
        print(cls, date_str)
        return numm

    @staticmethod
    def validity_check(date_str):
        day, month, year = map(int, date_str.split("-"))
        if day <= 31 and day != 0 and month <= 12 and month != 0 and year >= 2015 and year <= 2025:
            print(date_str)
            return day, month, year
        else:
            print("Неправильно введена дата(((")


add_data = input("Введите дату: ")
a = Date.conver(add_data)
b = Date.validity_check(add_data)