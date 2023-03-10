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
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def extract(cls, day_month_year):
        day_month_year = day_month_year.split('-')
        
        return (int(day_month_year[0]),
                int(day_month_year[1]),
                int(day_month_year[2]))
    
    def __str__(self):
        return f'Текущая дата {self.day_month_year}'
    
    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2023 >= year >= 0:
                    return 'Дата указана корректно'
                else:
                    return 'Неправильный год'
            else:
                return 'Неправильный месяц'
        return 'Неправильный день'


now = Data('10-03-2023')
print(now)
print(Data.valid(10, 3, 2030))
print(now.valid(10, 00, 2023))
print(now.valid(00, 00, 2023))
print(Data.extract('10-03-2023'))
print(now.extract('10-03-2023'))
print(Data.valid(10, 3, 2023))
