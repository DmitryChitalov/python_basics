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
    day_month_year = "26.03.2023"

    @classmethod
    def get_date(cls):
        data = [int(el) for el in str(cls.day_month_year).split(".")]
        cls.day, cls.month, cls.year = data
        return cls

    @staticmethod
    def check_date():
        message = []

        if not (2023 >= Date.year >= 0):
            message.append('неправильный год')
        if not (1 <= Date.month <= 12):
            message.append('неправильный месяц')
        if not (1 <= Date.day <= 31): #самый простой способ проверки для дней
            message.append('неправильный день')
        if len(message)== 0:
            message.append("Корректная дата")
        return '/'.join(message)


#d1 = Date("26.03.2023")
#print(d1.year)
Date.get_date()
print(f'день: {Date.day} ({type(Date.day)})')
print(f'день: {Date.month} ({type(Date.month)})')
print(f'день: {Date.year} ({type(Date.year)})')
print(Date.check_date())
