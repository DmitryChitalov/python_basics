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
from datetime import datetime


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def extract(cls, day_month_year):
        day, month, year = day_month_year.split("/")
        day = int(day)
        month = int(month)
        year = int(year)
        return day, month, year

    @staticmethod
    def validate(user_date):
        day, month, year = list(map(int, user_date.split("/")))
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2023 > year >= 0:
                    return f"Дата введена правильно"
                else:
                    return f"Ошибка - год указан неверно"
            else:
                return f"Ошибка - месяц указан неверно"
        else:
            return f"Ошибка - число указано неверно"


curent_date = datetime.now().date()
print(f'Текущая дата {curent_date.day}/{curent_date.month}/{curent_date.year}')
print(Data.extract("31/12/2022"))

print(Data.validate(input("Введите дату в формате дд/мм/год: ")))

