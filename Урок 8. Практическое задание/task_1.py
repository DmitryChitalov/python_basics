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
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        date = []

        for a in day_month_year.split():
            if a != '-':
                date.append(a)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31 and 1 <= month <= 12 and 1970 <= year <= 2023:
            return f'OK'
        else:
            return f'Неправильный ввод!'


print(Data.valid(1, 9, 2022))
print(Data.valid(32, 13, 2022))
print(Data.extract('30 - 8 - 2022'))
print(Data.extract('9 - 5 - 1945'))
