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

class OwnDate:
    def __init__(self, day_month_year):
        # self.day = day
        # self.month = month
        # self.year = year
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2099 >= year >= 0:
                    return f'Все ОК'
                else:
                    return f'Год некорректный'
            else:
                return f'Месяц некорректный'
        else:
            return f'День неверный'

    def __str__(self):
        return f'Дата на сегодня {OwnDate.extract(self.day_month_year)}'


today = OwnDate('2 - 3 - 2023')
print(today)
print(OwnDate.valid(33, 11, 2022))
print(today.valid(15, 18, 1990))
print(OwnDate.extract('31 - 12 - 2049'))
print(today.extract('03 - 03 - 2023'))
