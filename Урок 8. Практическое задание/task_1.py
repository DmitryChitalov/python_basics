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
    day_month_year = '32.11.2023'
    @classmethod
    def extraction(cls):
        date = cls.day_month_year.split('.')
        cls.day = int(date[0])
        cls.month = int(date[1])
        cls.year = int(date[2])
        print(f'{cls.day}.{cls.month}.{cls.year}')
    @staticmethod
    def validation(day, month, year):
        if day < 1 or day > 31:
            return print('День введен неверно!')
        if month < 1 or month > 12:
            return print('Месяц введен неверно!')
        if year < 1 or year > 2100:
            return print('Год введен неверно!')
        return print(f'{day}.{month}.{year}')
Date.extraction()
Date.validation(Date.day, Date.month, Date.year)
Date.validation(3, 13, 2065)
