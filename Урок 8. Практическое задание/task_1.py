"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
"""


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        data = []
        for el in day_month_year.split():
            if el != '-':
                data.append(el)
        return int(data[0]), int(data[1]), int(data[2])

    @staticmethod
    def validation(day, month, year):
        if day <= 31 and day > 0 and month <= 12 and month > 0 and year > 0:
            return 'Дата правильная'
        else:
            return 'Неверная дата'


print(Data.extract('11 - 05 - 2011'))
print(Data.validation(32, 22, 2022))
