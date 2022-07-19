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

from datetime import datetime

class Date:

    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def extract(cls, date):
        day, month, year = [int(el) for el in date.split(".")]
        return f'Число - {day}, месяц - {month}, год - {year}'

    @staticmethod
    def validate(day_month_year):
        try:
            datetime.strptime(day_month_year, '%d.%m.%Y')
            return "Дата верна"
        except ValueError:
            return "Дата не корректна!"


print(Date.validate('21.07.2022'))
print(Date.validate('32.07.2021'))
print(Date.validate('01.08.21'))
print(Date.extract('21.07.2022'))
