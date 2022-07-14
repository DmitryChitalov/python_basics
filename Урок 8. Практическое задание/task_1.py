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


class Data:
    day, month, year = None, None, None
    day_month_year = '13.07.2022'

    @classmethod
    def parse(cls):
        cls.day = int(cls.day_month_year.split('.')[0])
        cls.month = int(cls.day_month_year.split('.')[1])
        cls.year = int(cls.day_month_year.split('.')[2])

    @staticmethod
    def validate(day, month, year):
        return True if 1 <= day <= 31 and 1 <= month <= 12 and 1970 <= year <= 2022 else False


print(Data.validate(13, 7, 2022))
print(Data.validate(32, 0, 2022))
Data.parse()
print(Data.day)
print(Data.month)
print(Data.year)
