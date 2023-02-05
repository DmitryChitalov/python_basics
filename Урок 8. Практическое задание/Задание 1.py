"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором
@classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, date):
        self.date = date

    @classmethod
    def cm(cls, date):
        return cls([int(i) for i in date if i[0][0] != 0])

    @staticmethod
    def sm(date):
        return date[0] <= 31 and date[1] <= 12 and date[2] > 0


inp = input('Enter date with spaces: ')
cl = Data(inp.split())
cl_1 = cl.cm(inp.split())
print(f'DD {cl_1.date[0]} MM {cl_1.date[1]} YY {cl_1.date[2]}')
print(f'Validating of date is: {cl.sm(cl_1.date)}')

"""
Enter date with spaces: 10 08 2023
DD 10 MM 8 YY 2023
Validating of date is: True
"""
