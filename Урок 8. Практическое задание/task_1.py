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


class Date:
    day_month_year = "12.-12.-2022"

    @classmethod
    def to_extract(cls):
        day_month_year_split = map(int, cls.day_month_year.split("."))
        dmy_list = list(day_month_year_split)
        cls.day = dmy_list[0]
        cls.month = dmy_list[1]
        cls.year = dmy_list[2]

    @staticmethod
    def to_valid():
        if Date.day < 0 or Date.day > 31:
            print("Неверный номер дня")
        if Date.month < 0 or Date.month > 12:
            print("Неверный номер месяца")
        if Date.year < 0:
            print("Неверный номер года")


Date.to_extract()
Date.to_valid()
