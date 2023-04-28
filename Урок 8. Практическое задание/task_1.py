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
class Data:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def my_method(cls, day_month_year):
        s = day_month_year.split(sep='.')
        print(s)
        day = int(s[0])
        month = int(s[1])
        year = int(s[2])
        print(F"{day} / {month} / {year}")

    @staticmethod
    def valid_data(day_month_year):
        a = 0
        s = day_month_year.split(sep='.')
        if 0 < int(s[0]) < 13:
           a += 1
        if 0 < int(s[1]) < 32:
           a += 1
        if int(s[2]) == 2023:
           a += 1
        if a == 3:
           print(F"{s[0]} / {s[1]} / {s[2]}")
        else:
            print("Неверный формат")

Data.my_method("12.02.2023")

Data.valid_data("12.33.2023")