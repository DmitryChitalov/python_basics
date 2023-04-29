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

from calendar import monthrange
from datetime import datetime


class ErrorData(Exception):
    def __init__(self, user_data):
        self.user_data = user_data


class Data:
    day = None
    month = None
    year = None
    day_month_year = '41-04-2023'

    @classmethod
    def int_day_month_year(cls):
        data_list = cls.day_month_year.split('-')
        cls.day = int(data_list[0])
        cls.month = int(data_list[1])
        cls.year = int(data_list[2])

    @staticmethod
    def valid_check():
        try:
            if Data.month > 12:
                raise ErrorData('Месяц указан не корректно.')
        except ErrorData as ed:
            print(ed)

        else:
            days = monthrange(Data.year, Data.month)[1]
            try:
                if Data.day not in [i for i in range(1, days+1)]:
                    raise ErrorData('День указан не корректно.', )
            except ErrorData as ed:
                print(ed)
            else:
                try:
                    if Data.year > datetime.now().year:
                        raise ErrorData('Год указан не корректно.')
                except ErrorData as ed:
                    print(ed)
                else:
                    pass  # Next code for program


Data.int_day_month_year()
Data.valid_check()
