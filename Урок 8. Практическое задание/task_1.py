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
    day_month_year = ""

    @classmethod
    def set_date(self, date):
        day, month, year = map(int, date.split("."))
        self.day_month_year = (day, month, year)

    @staticmethod
    def valid_date(date):
        day, month, year = map(int, date.split('.'))
        if month < 1 or month > 12 or day < 1 or day > 31 or month == 2 and day > 29 \
                or month in [4, 6, 9, 11] and day > 30:
            return print("Неверная дата!")
        else:
            return print("Дата верна!")


Date.set_date("09.04.2023")
print(Date.valid_date("09.04.2023"))
day, month, year = Date.day_month_year
print(day, month, year)
