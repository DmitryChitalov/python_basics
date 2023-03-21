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
import time

class Date():
    day_month_year: str

    @classmethod
    def convert_date(cls):
        my_date = cls.day_month_year.split('.')
        return f'Число: {int(my_date[0])}, Месяц: {int(my_date[1])}, Год: {int(my_date[2])}'

    @staticmethod
    def is_valid(day_month_year):
        try:
            time.strptime(day_month_year, '%d.%m.%Y')
            return 'Дата верная'
        except ValueError:
            return 'Неверная дата'

Date.day_month_year = input('Введите число в формате dd.mm.yyyy: ')
print(Date.convert_date())
print(Date.is_valid(Date.day_month_year))