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


class MyDate:
    day_month_year = None

    def __init__(self, day_month_year):
        MyDate.day_month_year = day_month_year

    @classmethod
    def parse(cls):
        dmy = MyDate.day_month_year.split("-")
        day = int(dmy[0])
        month = int(dmy[1])
        year = int(dmy[2])
        return f"День:{day} Месяц:{month} Год:{year}"

    @staticmethod
    def valid():
        try:
            dmy = MyDate.day_month_year.split("-")
            day = int(dmy[0])
            month = int(dmy[1])
            year = int(dmy[2])
            return "Дата корректна" if day >= 1 | day <= 31 | month >= 1 | month <= 12 | year >= 1990 | year <= 9999 \
                else "Дата не корректна"
        except ValueError:
            return "Дата не корректна"


print(MyDate("1-5-2022").parse())
print(MyDate("25-5-2022").parse())
print(MyDate("25-5-2022").valid())
print(MyDate("250-5-2022").valid())
