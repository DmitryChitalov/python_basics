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

from datetime import date


class Data:
    day_month_year = "28 - 03 - 2023"

    @classmethod
    def extract(cls):
        my_date = [int(el) for el in cls.day_month_year.split() if el != '-']
        cls.day, cls.month, cls.year = my_date
        return my_date

    @staticmethod
    def valid():
        if 1 <= Data.day <= 31:
            if 1 <= Data.month <= 12:
                if 2099 >= Data.year >= 0:
                    return f"Все в порядке"
                else:
                    return f"Неправильный год"
            else:
                return f"Неправильный месяц"
        else:
            return f"Неправильный день"


print(Data.extract())
print(Data.valid())
