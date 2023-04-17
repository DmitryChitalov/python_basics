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

    day_month_year = input(f"Введите дату ДД.ММ.ГГГГ: ")

    @classmethod
    def date_convert(cls):
        Date.day_month_year = Date.day_month_year.split(".")
        Date.d   = int(Date.day_month_year[0])
        Date.m = int(Date.day_month_year[1])
        Date.y = int(Date.day_month_year[2])

    @staticmethod
    def date_check(dd, mm, yyyy):
        try:
            if 0 < dd < 32 and 0 < mm < 13 and 1000 < yyyy < 2024:
                print('Дата корректна')
            else:
                print('Дата некорректна')
        except ValueError:
            print('Ошибка!')

Date.date_convert()
Date.date_check(Date.d, Date.m, Date.y)
