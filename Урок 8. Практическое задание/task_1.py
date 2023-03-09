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
    def __init__(self, day_month_year: str):
        self.day_month_year = day_month_year
    
    @classmethod
    def extraction_day_month_year(cls, obj):
        obj.day = int(obj.day_month_year.split('-')[0])
        obj.month = int(obj.day_month_year.split('-')[1])
        obj.year = int(obj.day_month_year.split('-')[2])
        return obj
    
    @staticmethod
    def validity_check(obj):
        if  obj.day < 1 or obj.day > 31 :
            print(f'{obj.day} - некорректный день.')
        elif obj.month < 1 or obj.month > 12:
            print(f'{obj.month} - некорректный месяц.')
        elif obj.year < 2000 or obj.year > 2023:
            print(f'{obj.year} - некорректный год.')   
        else:
            print('Дата корректна.')
    

date = Date('09-03-2023')
Date.extraction_day_month_year(date)
print(date.__dict__)
print(f'День: {date.day}, месяц: {date.month}, год: {date.year}.')

Date.validity_check(date)
