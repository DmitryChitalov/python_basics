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
    day_month_year = ''
    day = 0
    month = 0
    year = 0

    @classmethod
    def parse_data(cls, day_month_year):
        cls.day_month_year = day_month_year
        parts = cls.day_month_year.split('.')
        cls.day = int(parts[0])
        cls.month = int(parts[1])
        cls.year = int(parts[2])

    @staticmethod
    def validate_data():
        print(Data.day_month_year)
        print(Data.day)
        print(Data.month)
        print(Data.year)
        if Data.year < 0:
            print('Некорректный год')
            pass
        if Data.month < 1 or Data.month > 12:
            print('Некорректный месяц')
            pass
        is_leap = Data.year % 4 == 0
        months = {1: 31, 2: 28 if is_leap == False else 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
                  11: 30, 12: 31}
        if (Data.day < 1 or Data.day > months[Data.month]):
            print('Некорректный день')
            pass


Data.parse_data('28.02.2023')
Data.validate_data()
