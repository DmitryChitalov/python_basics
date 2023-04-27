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


import re


class Date:
    max_days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    max_days_in_month_ly = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, date_string):
        match_result = re.match(r'^\d\d-\d\d-\d\d\d\d$', date_string)
        if match_result is None:
            raise Exception(f'{date_string} - неверный формат, используйте дд-мм-гггг')
        self.date_string = date_string
        self.day, self.month, self.year = map(int, date_string.split('-'))

    @classmethod
    def extract(cls, date_string):
        date = cls(date_string)
        return [date.day, date.month, date.year]

    @staticmethod
    def validate(date_string):
        date = Date(date_string)
        is_not_zero = date.day > 0 and date.month > 0 and date.year > 0
        if date.year % 4 == 0 and date.year % 100 != 0 or date.year % 400 == 0:
            is_fit_boundaries = date.month <= 12 and date.day <= date.max_days_in_month_ly[date.month - 1]
        else:
            is_fit_boundaries = date.month <= 12 and date.day <= date.max_days_in_month[date.month - 1]
        return is_not_zero and is_fit_boundaries


if __name__ == '__main__':
    real_date_str = '22-12-1983'
    not_valid_date_str = '29-02-2019'
    incorrect_date_str = '9-02/*019'

    real_date = Date(real_date_str)
    print(f'{real_date.extract(real_date_str)} - извлеченное значение')

    not_valid_date = Date(not_valid_date_str)
    print(f'{real_date.extract(not_valid_date_str)} - извлеченное значение')

    try:
        incorrect_date = Date(incorrect_date_str)
    except Exception as e:
        print(e)

    if Date.validate(real_date_str):
        print(f'{real_date_str} - корректное значение')
    else:
        print(f'{real_date_str} - некорректное значение')

    if Date.validate(not_valid_date_str):
        print(f'{not_valid_date_str} - корректное значение')
    else:
        print(f'{not_valid_date_str} - некорректное значение')
