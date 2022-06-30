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
    def __init__(self, dd_mm_yyyy):
        self.dd_mm_yyyy = str(dd_mm_yyyy)

    @classmethod
    def transform(cls, dd_mm_yyyy):
        test_date = []

        for i in dd_mm_yyyy.split():
            if i != '-': test_date.append(i)

        return int(test_date[0]), int(test_date[1]), int(test_date[2])

    @staticmethod
    def validate(dd, mm, yyyy):

        if 1 <= dd <= 31:
            if 1 <= mm <= 12:
                if 2999 >= yyyy >= 0:
                    return f'Дата корректна'
                else:
                    return f'Неверно указан год'
            else:
                return f'Неверно указан месяц'
        else:
            return f'Неверно указан день'

    def __str__(self):
        return f'Текущая дата {Date.transform(self.dd_mm_yyyy)}'


date = Date('29 - 05 - 2022')
print(date)
print(Date.transform('21 - 11 - 2001'))
print(Date.validate(1, 12, 2022))
print(Date.validate(100, 12, 2022))
print(Date.validate(10, 120, 2022))
print(Date.validate(10, 12, 20222))
