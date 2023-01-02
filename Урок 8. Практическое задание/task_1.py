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
    def __init__(self):
        print(f"Your date is: {self}")

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split("-"):
            if i != '-':
                my_date.append(i)

        day = int(my_date[0])
        month = int(my_date[1])
        year = int(my_date[2])

        return day, month, year

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2023 >= year >= 0:
                    print("Your date is OK")
                else:
                    print("Year error")
            else:
                print("Month error")
        else:
            print("Day error")


today = input("Enter your date: ")
Data.__init__(today)
day, month, year = Data.extract(today)
Data.valid(day, month, year)
