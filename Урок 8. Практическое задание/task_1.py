'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''
import datetime

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def extractor(cls, d):
        if Date.validator(d):
            return datetime.date(int(d[6:]), int(d[3:5]), int(d[:2]))
        else:
            print('Проверьте формат даты')

    @staticmethod
    def validator(d):
        try:
            datetime.date(int(d[6:]), int(d[3:5]), int(d[:2]))
            return True
        except ValueError:
            return False

print("1")
print(Date.extractor('30-01-2023'))
print(Date.validator('30-01-2023'))
print("2")
print(Date.extractor('01-30-2023'))
print(Date.validator('01-30-2023'))
print("3")
print(Date.extractor('30-01-2023'))
print(Date.validator('30-01-2023'))
print("4")
print(Date.extractor('01-30-2023'))
print(Date.validator('01-30-2023'))