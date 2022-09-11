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
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f"Введенные данные корректны"
                else:
                    return f"Некорректно указан год"
            else:
                return f"Некорректно указан месяц"
        else:
            return f"Некорректно указан день"

    def __str__(self):
        return f"Текущая дата {Date.extract(self.day_month_year)}"


today = Date("1 - 9 - 2022")
print(today)
print(Date.valid(31, 12, 2022))
print(Date.extract("31 - 12 - 2022"))
print(today.valid(7, 15, 2011))
print(today.extract("1 - 9 - 2011"))
