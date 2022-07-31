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

    day_month_year = "31 - 7 - 2022"

    @classmethod
    def extract(cls):
        current_date = [int(el) for el in cls.day_month_year.split() if el != '-']
        cls.day, cls.month, cls.year = current_date

    @staticmethod
    def valid():

        if 1 <= Date.day <= 31:
            if 1 <= Date.month <= 12:
                if 2022 >= Date.year >= 0:
                    return f"Дата указана верно"
                else:
                    return f"Неправильный год"
            else:
                return f"Неправильный месяц"
        else:
            return f"Неправильный день"


Date.extract()
print(Date.valid())
