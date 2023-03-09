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
    @classmethod
    def date_parsing(cls, param):
        date = [int(el) for el in param.split('.')]
        cls.validate(date)
        cls.day = date[0]
        cls.month = date[1]
        cls.year = date[2]

    @staticmethod
    def validate(date):
        if date[0] > 31 or date[0] < 1:
            raise Exception('Неверно указана число!')
        if date[1] > 12 or date[1] < 1:
            raise Exception('Неверно указан месяц!')
        if date[2] > 2023 or date[2] < 1900:
            raise Exception('Неверно указан год!')


d1 = Date()
try:
    d1.date_parsing('13.12.2025')
    print(f'День = {d1.day}')
    print(f'Месяц = {d1.month}')
    print(f'Год = {d1.year}')
except Exception as err:
    print(err)
