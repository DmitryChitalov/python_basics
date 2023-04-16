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
    day_month_year = "25 - 11 - 2022"

    @classmethod
    def extract(cls):
        date_date = [int(el) for el in cls.day_month_year.split() if el != "-"]
        cls.day, cls.month, cls.year = date_date
    @staticmethod
    def valid():
        if 1 <= Data.day <= 25:
            if 1 <= Data.month <= 11:
                if 2022 >= Data.year >= 0:
                    return f"Верная дата"
                else:
                    return f"Неправильная дата"
Data.extract()
print(Data.valid())

