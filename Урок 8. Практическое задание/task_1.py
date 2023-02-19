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

    @classmethod
    def my_method(self, dmy):
        d = dmy.split("-")
        self.day, self.month, self.year = dmy.split("-")

    @staticmethod
    def valid():
        if 1 <= int(Date.day) <= 31:
            if 1 <= int(Date.month) <= 12:
                if 2023 >= int(Date.year) >= 0:
                    return f'Правильная дата'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

d = Date()
d.my_method('31-14-2023')
print(d.valid())
