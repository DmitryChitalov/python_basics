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
import re


class Date:
    day_month_year = ''

    def __init__(self, day_month_year):
        Date.day_month_year = day_month_year

    @classmethod
    def extract(cls):
        cls.day, cls.month, cls.year = [int(x) for x in re.findall(r'\d+', cls.day_month_year)]

    @staticmethod
    def validate(day, month, year):
        if month not in range(1, 12 + 1):
            return 1

        if year % 4 == 0:
            if month == 2 and day not in range(1, 29 + 1):
                return 2
        else:
            if month == 2 and day not in range(1, 28 + 1):
                return 3

        if (month in [1, 3, 5, 7, 8, 10, 12] and day not in range(1, 31 + 1)) or (
                month in [4, 6, 9, 11] and day not in range(1, 30 + 1)):
            return 4

        return 0


dates = ['1_3_2020', '29/2/2020', '32.12.2022', '16_13_2011', '29_02.2021', '01.01.2002']

for date_string in dates:
    dt = Date(date_string)
    print(f"Date string: {dt.day_month_year}")
    dt.extract()
    print(f"Extracted data: day={dt.day}, month={dt.month}, year{dt.year}")
    status = Date.validate(day=dt.day, month=dt.month, year=dt.year)
    if status == 0:
        print("Date valid")
    elif status == 1:
        print("Month is not valid")
        pass
    else:
        print(f"Day is not valid (rc={status})")
