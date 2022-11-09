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

    day = 0
    month = 0
    year = 0
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def method_1(cls, day_month_year):
        date = []
        for i in day_month_year.split('.'):
            date.append(i)
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
        print (day,month, year)
        cls.method_2(day, month, year)

    @staticmethod
    def method_2(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year:
                    result_date = f'{day} - {month} - {year}'
                    print(f'Дата корректна - выбрана дата {result_date}')
                else: print(f'Некорректный год')
            else: print(f'Некорректный месяц')
        else: print(f'Некорректная дата')


Date.method_1('133.11.2033')
c1 = Date
print(c1.method_1('10.11.2033'))
