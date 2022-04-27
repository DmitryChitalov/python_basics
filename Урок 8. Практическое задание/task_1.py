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

from typing import List


class MyDate:
    day_month_year:str = "01.01.2022"

    @classmethod
    def parse_date(self):
        date_parts = MyDate.day_month_year.split(".")
        day = int(date_parts[0])
        month = int(date_parts[1])
        year = int(date_parts[2])
        self.validate(day, month, year)

        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def validate(day, month, year):
        month_31_day = [1, 3, 5, 7, 8, 10, 12]
        month_extra = 2

        if year < 0:
            raise ValueError("Year can't be less than 0")

        if month < 0 or month > 12:
            raise ValueError("Month must be in the range 1-12")

        if day < 0 and day > 31:
            raise ValueError("Day must be in range 1-31")

        if month == month_extra:
            if year % 4 == 0 and day > 29:
                raise ValueError("Day mus be in range 1-29")
            elif year % 4 != 0 and day > 28:
                raise ValueError("Day mus be in range 1-28")
        elif month_31_day.index(month) < 0 and day > 30:
            raise ValueError("Day can't be greater than 30")

        print("Success validate")



MyDate.parse_date()
MyDate.validate(MyDate.day, MyDate.month, MyDate.year)