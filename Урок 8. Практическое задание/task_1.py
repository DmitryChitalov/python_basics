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


class MyDate:
    day_month_year = ''
    day = 0
    month = 0
    year = 0
    date_ok = True

    @classmethod
    def date_parse(cls):
        MyDate.day = int(MyDate.day_month_year.split('_')[0])
        MyDate.month = int(MyDate.day_month_year.split('_')[1])
        MyDate.year = int(MyDate.day_month_year.split('_')[2])

    @staticmethod
    def date_validation():
        if (MyDate.day <= 0) or (MyDate.day > 31) or (MyDate.day > 29 and MyDate.month == 2) or (
                MyDate.day == 31 and MyDate.month not in (1, 3, 5, 7, 8, 10, 12)) or (
                MyDate.day == 29 and MyDate.month == 2 and MyDate.year % 4 > 0):
            print("Неверно задан день")
            MyDate.date_ok = False
        if (MyDate.month <= 0) or (MyDate.month > 12):
            print("Неверно задан месяц")
            MyDate.date_ok = False
        if MyDate.year <= 0:
            print("Неверно задан год")
            MyDate.date_ok = False


MyDate.day_month_year = '29_02_2020'
MyDate.date_parse()
MyDate.date_validation()
if MyDate.date_ok:
    print(f"Число:{MyDate.day}, Месяц: {MyDate.month}, Год: {MyDate.year}")
