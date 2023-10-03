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


class OwnDate:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        date = []

        for i in day_month_year.split():
            if i != '-':
                date.append(i)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):

        if day not in range(1, 32):
            return f'День указан некорретно'
        if month not in range(1, 13):
            return f'Месяц укaзан некорретно'
        if year not in range(0, 2100):
            return f'Год указан некорретно'
        return f'Данные укaзаны корректно'

    def __str__(self):
        return f'Дата на сегодня {OwnDate.extract(self.day_month_year)}'


today = OwnDate('22 - 6 - 2023')
print(today)
print(OwnDate.valid(31, 11, 2022))
print(today.valid(15, 18, 1990))
print(OwnDate.extract('31 - 9 - 2021'))
print(today.extract('22 - 6 - 2023'))
