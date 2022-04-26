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


# 1ая часть задания
class MyData:
    day_month_year = datetime.now()

    @classmethod
    @property  # для того, чтобы сделать атрибутом
    def get_day(MyData):
        my_day = MyData.day_month_year.day
        return my_day


print(MyData.get_day)  # вызов через класс
example2 = MyData()
print(example2.get_day)  # вызов через объект и метод как атрибута


# 2ая часть задания
class MyData2:
    day_month_year2 = "31_12_2022"

    @staticmethod
    def valid_day():
        my_list = MyData2.day_month_year2.split("_")
        if int(my_list[0]) > 31:
            print("Неверное число!")
        elif int(my_list[1]) > 12:
            print("Неверный месяц!")
        elif int(my_list[2]) > 3000:
            print("Неверный год!")
        else:
            print(f"Ваша дата: {my_list[0]}.{my_list[1]}.{my_list[2]}")


MyData2.valid_day()

# Сделала через два класса, так как проводить валидацию, используя класс datatime, не имеет смысла
