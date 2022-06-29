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
    day_month_year = "11-12-2017"

    @classmethod
    def extract(cls):
        my_date = [int(el) for el in cls.day_month_year.split('-')]
        cls.day, cls.month, cls.year = my_date

    @staticmethod
    def valid():
        if 1 < Data.day > 31:
            return f"Неправильный день"
        elif 1 < Data.month > 12:
            return f"Неправильный месяц"
        elif 2017 > Data.year < 0:
            return f"Неправильный год"
        else:
            return f"Формат даты правильный"


Data.extract()
print(Data.valid())
