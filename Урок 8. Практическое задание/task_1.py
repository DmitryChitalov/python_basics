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
    day_month_year = ""

    @classmethod
    def extract_date(cls, date_string):
        day, month, year = date_string.split("/")
        cls.day_month_year = int(day), int(month), int(year)

    @staticmethod
    def validate_date(day, month, year):
        if not (1 <= month <= 12):
            return False
        if month in {1, 3, 5, 7, 8, 10, 12}:
            return 1 <= day <= 31
        elif month in {4, 6, 9, 11}:
            return 1 <= day <= 30
        else:
            # February
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                # Leap year
                return 1 <= day <= 29
            else:
                return 1 <= day <= 28

Date.extract_date("25/07/2018")
print(Date.day_month_year)  # (23, 9, 2022)

print(Date.validate_date(31, 12, 2021))  # True
print(Date.validate_date(31, 4, 2021))  # False
print(Date.validate_date(29, 2, 2024))  # True
print(Date.validate_date(29, 2, 2023))  # False
