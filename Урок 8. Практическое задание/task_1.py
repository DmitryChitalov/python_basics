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
    day_month_year = ''

    @classmethod
    def set_date(cls, date_string):
        day, month, year = date_string.split('.')
        cls.day_month_year = int(day), int(month), int(year)

    @staticmethod
    def is_valid_date(date_string):
        day, month, year = map(int, date_string.split('.'))
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        if month == 2 and day > 29:
            return False
        if month in [4, 6, 9, 11] and day > 30:
            return False
        if year < 1900 or year > 2100:
            return False
        return True


date_string = '15.02.2022'
if Date.is_valid_date(date_string):
    Date.set_date(date_string)
    print(Date.day_month_year) # (15, 2, 2022)
else:
    print('Invalid date')
