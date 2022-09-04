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
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def date_to_int(cls, day_month_year):
        datelist = list(day_month_year.split("-"))
        day = int(datelist[0])
        month = int(datelist[1])
        year = int(datelist[2])
        return day, month, year

    @staticmethod
    def date_validate(mydate):
        if 1 < mydate[0] > 31:
            return f"Invalid \'Day\' value in \'Date\' format"
        elif 1 < mydate[1] > 12:
            return f"Invalid \'Month\' value in \'Date\' format"
        else:
            return f"Valid"


print(MyDate.date_to_int("01-02-1999"))
print(MyDate.date_validate(MyDate.date_to_int("32-02-1999")))
