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
    def transform(cls, day_month_year):
        test_date = []

        for i in day_month_year.split():
            if i != '-': test_date.append(i)

        return int(test_date[0]), int(test_date[1]), int(test_date[2])

    @staticmethod
    def validate(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2999 >= year >= 0:
                    return f'Дата корректна'
                else:
                    return f'Неверный год'
            else:
                return f'Неверный месяц'
        else:
            return f'Неверный день'

    def __str__(self):
        return f'Текущая дата {Date.transform(self.day_month_year)}'


date = Date('30 - 07 - 2022')

print(date)
print(Date.transform('30 - 07 - 2022'))
print(Date.validate(10, 10, 2022))
print(Date.validate(50, 11, 2022))
print(Date.validate(5, 150, 2022))
print(Date.validate(10, 10, 20222))