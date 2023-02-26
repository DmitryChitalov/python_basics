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
    def __init__(self, data_1):
        self.data_1 = str(data_1)

    @classmethod
    def extract(cls, data_1):
        my_date = []

        for i in data_1.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if year >= 0:
                    return f'Ввод корректен'
                else:
                    return f'Некорректный год'
            else:
                return f'Некорректный месяц'
        else:
            return f'Некорректный день'



print(Data.valid(11, 11, 2023))
print(Data.valid(1, 17, 2007))
print(Data.extract('11 - 3 - 2023'))