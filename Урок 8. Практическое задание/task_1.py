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
        date_new = []
        for i in day_month_year.split('-'):
            date_new.append(i)
        return int(date_new[0]), int(date_new[1]), int(date_new[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return 'Дата указан верно'
                else:
                    return 'Неправильный год'
            else:
                return 'Неправильный месяц'
        else:
            return 'Неправильный день'

    def __str__(self):
        return f'Текущая дата: \n {Data.extract(self.day_month_year)}'


date_1 = Data('28 - 7 - 2022')
print(date_1)
print(date_1.valid(10, 22, 1993))
print(date_1.extract('28 - 07 - 2022'))
print(Data.extract('28 - 07 - 2022'))
print(Data.valid(1, 11, 2000))
