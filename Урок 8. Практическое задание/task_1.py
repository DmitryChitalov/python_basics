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
    """класс «Дата»"""
    day_month_year = "10/12/2022"

    @classmethod
    def to_split(cls):
        """
        извлекает число, месяц, год, преобразовывает их тип к типу «Число»
        и делает атрибутами класса
        """
        parts = cls.day_month_year.split("/")
        cls.day = int(parts[0])
        cls.month = int(parts[1])
        cls.year = int(parts[2])

    @staticmethod
    def validate_date():
        """
        проводит валидацию числа, месяца и года
        """
        Date.to_split()
        if Date.year < 1950 or Date.year > 2022:
            raise ValueError(f"Invalid year={Date.year}")
        if Date.month < 1 or Date.month > 12:
            raise ValueError(f"Invalid month={Date.month}")
        if Date.day < 1 or Date.day > 31:
            raise ValueError(f"Invalid day={Date.day}")


print(f"test {Date.day_month_year}")
Date.to_split()
print(f"split date>> year={Date.year}, month={Date.month}, day={Date.day}")

Date.day_month_year = "10/13/2022"
print(f"validate {Date.day_month_year} is ", end='')
try:
    Date.validate_date()
except ValueError as e:
    print(f"error! {e.args[0]}")
else:
    print("Ok")
