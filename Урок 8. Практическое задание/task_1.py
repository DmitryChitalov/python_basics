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
    day_month_year = '30-06-2022'

    @classmethod
    def extract_date(cls):
        date = [int(el) for el in cls.day_month_year.split('-')]
        cls.day, cls.month, cls.year = date

    @staticmethod
    def check_date():
        try:
            try_date = datetime.date(Date.year, Date.month, Date.day)
            print('Дата корректна')
        except:
            print('Введенная дата некорректна')

Date.extract_date()
Date.check_date()