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


class My_Date:
    day_month_year = "30_05_1993"

    @classmethod
    def user_count(cls):
        my_date = My_Date.day_month_year.split("_")
        My_Date.day = int(my_date[0])
        My_Date.month = int(my_date[1])
        My_Date.year = int(my_date[2])
        print(f"День {My_Date.day}, Месяц {My_Date.month},Год {My_Date.year}")

    @staticmethod
    def valid():
        if My_Date.day > 1 and My_Date.day < 31 and My_Date.month > 1 and My_Date.month < 12 and My_Date.year > 1900 and My_Date.year < 2022:
            print("Дата указано корректно")
        else:
            print("Дата указано некорректно")


my_date = My_Date()
My_Date.user_count()
My_Date.valid()
