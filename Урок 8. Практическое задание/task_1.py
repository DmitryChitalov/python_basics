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
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def extract(cls, date):
        if Date.validate(date):
            return datetime.date(int(date[6:]), int(date[3:5]), int(date[:2]))
        else:
            print('Не правильный формат')

    @staticmethod
    def validate(date):
        try:
            datetime.date(int(date[6:]), int(date[3:5]), int(date[:2]))
            return True
        except ValueError:
            return False

print("1")
print(Date.extract('29-02-2023'))
print(Date.validate('29-02-2023'))
print("2")
print(Date.extract('08-02-2023'))
print(Date.validate('08-02-2023'))
print("3")
print(Date.extract('2023-02-08'))
print(Date.validate('2023-02-08'))
print("4")
print(Date.extract('02-29-2023'))
print(Date.validate('02-29-2023'))