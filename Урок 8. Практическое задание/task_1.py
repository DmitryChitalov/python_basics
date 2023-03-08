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
    day_month_year = None

    @classmethod
    def set_date(cls, date_string):
        day, month, year = map(int, date_string.split('.'))
        cls.day_month_year = (day, month, year)

    @staticmethod
    def is_valid(day, month, year):  # простая валидация значений
        if not (1 <= month <= 12):
            return False
        if month in [4, 6, 9, 11] and day > 30:
            return False
        if month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                if day > 29:
                    return False
            else:
                if day > 28:
                    return False
        return True


# > Проверить работу полученной структуры на реальных данных

# Создание объекта класса "Date" и установка значения атрибута "day_month_year"
Date.set_date('08.03.2023')

# Вывод значения атрибута "day_month_year"
print(Date.day_month_year)  # (8, 3, 2023)

# Проверка валидности даты
print(Date.is_valid(29, 2, 2020))  # True
print(Date.is_valid(29, 2, 2021))  # False
print(Date.is_valid(31, 4, 2022))  # False
print(Date.is_valid(31, 5, 2023))  # True
