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
    day_month_year = '12.09.2022'

    @classmethod
    def date_splitter(cls):
        spl = cls.day_month_year.split(".")
        cls.day = int(spl[0])
        cls.month = int(spl[1])
        cls.year = int(spl[2])
        print(f"День: {cls.day}, месяц: {cls.month}, год: {cls.year}")

    @staticmethod
    def validate_for_date(day, month, year):
        if day < 1 or day > 31:
            print("Диапозон дней месяца выходит за рамки!")
        if month < 1 or month > 12:
            print("Диапозон месяца выходит за рамки!")
        if year < 1900 or year > 2100:
            print("Врят ли нам пригодится данный год от Рождества Христова!")
        print(f"День: {day}, месяц: {month}, год: {year}")


Data.date_splitter()
Data.validate_for_date(Data.day, Data.month, Data.year)

Data.validate_for_date(45, 15, 2122)

