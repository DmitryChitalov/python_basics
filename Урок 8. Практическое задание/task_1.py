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
    day: int
    month: int
    year: int

    def __init__(self, date_string: str):
        numbers = Date.extract_numbers(date_string)
        self.validate_numbers(numbers)

        self.day, self.moth, self.year = numbers

    @classmethod
    def extract_numbers(cls, date_string: str) -> list:
        return [int(x) for x in date_string.split('-')]

    @staticmethod
    def validate_numbers(numbers: list):
        d, m, y = numbers

        assert 1 <= d <= 31, "wrong day format"
        assert 1 <= m <= 12, "wrong month format"
        assert 1913 <= y <= 2050, "wrong year format"


date_enter = Date('07-07-2007')
