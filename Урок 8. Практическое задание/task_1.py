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
    day_month_year: str

    def __init__(self, str_represent: str):
        self.day_month_year = str_represent

    @classmethod
    def convert_to_number(cls, day_month_year):
        my_date = []

        for i in day_month_year.split('-'):
            my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def is_valid(date: str):
        number_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        parsed_date = date.split('-')
        day, month, year = map(int, parsed_date)
        if month < 1 or month > 12 or day > number_of_days[month - 1] or year < 0 or year > 2022:
            return False
        return True

    def __str__(self):
        return f'Current date: {Date.convert_to_number(self.day_month_year)}'


today = Date('09-06-2022')
print(today)
print(Date.is_valid('11-11-2022'))
print(today.is_valid('11-13-2011'))
print(Date.convert_to_number('11-11-2011'))
print(today.convert_to_number('11-11-2020'))
print(Date.is_valid('29-02-2020'))
