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
from datetime import date


class MyDate:
    year_month_day = '1970-41-01'

    @classmethod
    def make_atr(cls):
        entered_date = input('Введите дату в формате yyyy-mm-dd: ')
        cls.year = int(entered_date[0:4])
        cls.month = int(entered_date[5:7])
        cls.day = int(entered_date[8:10])
        return cls.year, cls.month, cls.day

    @staticmethod
    def validation(input_date):
        try:
            year, month, day = input_date.split('-')
            date(int(year), int(month), int(day))
            return 'Дата существует'
        except ValueError:
            year, month, day = input_date.split('-')
            print(int(year), int(month), int(day))
            return 'Вы указали неправильный формат даты'


a = MyDate
a.make_atr()
print(a.year)
print(a.month)
print(a.day)
print(a.validation('1990-11-41'))
