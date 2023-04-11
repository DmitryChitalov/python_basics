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

    def __init__(self, day_month_year):
        pass

    @classmethod
    def first_func(cls, day_month_year):
        ex_list = day_month_year.split('.')
        day = int(ex_list[0])
        month = int(ex_list[1])
        year = int(ex_list[2])
        return print(f'День: {day}, Месяц: {month}, Год: {year}')

    @staticmethod
    def second_func(day_month_year):
        ex_list = day_month_year.split('.')

        if int(ex_list[0]) > 31 or int(ex_list[1]) > 12 or int(ex_list[2]) > 2023:
            return print('В дате ошибка! Валидация не пройдена')
        else:
            return print('Валидация пройдена!')


Date.first_func('10.10.2010')
Date.second_func('10.13.2010')
Date.second_func('10.11.2010')
Date.first_func('23.10.2020')
