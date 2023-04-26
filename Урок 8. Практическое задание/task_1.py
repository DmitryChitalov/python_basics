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
    def __init__(self, dates):
        self.dates = str(dates)

    @classmethod
    def date_list(cls, dates):
        date_numbers = []
        for i in dates.split():
            if i != "-":
                date_numbers.append(i)
        return int(date_numbers[0]), int(date_numbers[1]), int(date_numbers[2])

    @staticmethod
    def check_date(day, month, year):
        if 0 < day < 32 and 0 < month < 13 and year == 2023:
            return 'Правильная дата'
        else:
            return 'Неверная дата'


today = Date("26 - 04 - 2023")
print(today.date_list("26 - 04 - 2023"))
print(today.check_date(11, 12, 2023))
print(today.check_date(11, 13, 2023))
