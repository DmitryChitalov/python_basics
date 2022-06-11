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
    day_month_year = '11-06-2022'

    @classmethod
    def extract(cls):
        day, month, year = cls.day_month_year.split('-')
        day = int(day)
        month = int(month)
        year = int(year)
        return day, month, year

    @staticmethod
    def data(d, m, y):
        if 1 <= d <= 31:
            if 1 <= m <= 12:
                if 2023 > y >= 0:
                    return f'Корректный ввод'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

a = Data.extract()
b = Data.data(a[0], a[1], a[2])
print(b)