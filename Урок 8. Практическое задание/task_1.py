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

    def __init__(self, date):
        self.day_month_year = date

    @classmethod
    def make_attributes(cls, date):
        temp_list = date.split('-')
        Data.day = int(temp_list[0])
        Data.month = int(temp_list[1])
        Data.year = int(temp_list[2])

    @staticmethod
    def validate():
        if Data.day not in range(1, 31):
            return "imposible day num"
        if Data.month not in range(1, 12):
            return "imposible day month"
        if Data.year <= 0:
            return "imposible day year"
        return f"current date is: {Data.day}/{Data.month}/{Data.year}"

#    def __str__(self):
 #       print(f"Date is {Data.make_attributes}")


Data.make_attributes("10-04-2023")
print(Data.validate())
