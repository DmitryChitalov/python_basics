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
    day_month_year = 'dd-mm-YYYY'

    @classmethod
    def create_fragments(cls):
        cls.day = int(cls.day_month_year[:2])
        cls.month = int(cls.day_month_year[3:5])
        cls.year = int(cls.day_month_year[6:])

    @staticmethod
    def is_date(day=-1, month=-1, year=-1):
        try:
            datetime(day=day, month=month, year=year)
            return True
        except TypeError:
            return False
        except ValueError:
            return False


d = Date()

Date.day_month_year = '31-11-2023'
Date.create_fragments()
print(f"{d.day_month_year=} {d.day=} {d.month=} {d.year=}")
print(Date.is_date(day=d.day, month=d.month, year=d.year))

Date.day_month_year = '31-12-2023'
Date.create_fragments()
print(f"{d.day_month_year=} {d.day=} {d.month=} {d.year=}")
print(Date.is_date(day=d.day, month=d.month, year=d.year))
