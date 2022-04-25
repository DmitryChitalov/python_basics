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

from datetime import datetime


class Data:
    day_month_year = '11-05-2022'

    @classmethod
    def extract(cls):
        if cls.valid(cls.day_month_year):
            day, month, year = map(int, cls.day_month_year.split('-'))
            setattr(cls, 'c_day', day)
            setattr(cls, 'c_month', month)
            setattr(cls, 'c_year', year)
            return f'{Data.c_day:02}-{Data.c_month:02}-{Data.c_year:04}'
        return 'Ошибка ввода'

    @staticmethod
    def valid(data):
        try:
            if data == datetime.strptime(data, "%d-%m-%Y").strftime('%d-%m-%Y'):
                return True
        except ValueError:
            print("Некорректные данные или ввод, дата должна быть в формате: dd-mm-yyyy")
            return False


d = Data
print(d.extract())
d.day_month_year = '29-02-2022'
print(d.extract())
