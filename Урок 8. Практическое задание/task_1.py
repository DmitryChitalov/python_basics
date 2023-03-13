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
from datetime import date

class Date:
    def __init__(self, usr_date):
        self.usr_date = usr_date

    @classmethod
    def get_dmy(cls, usr_date):
        day = int(usr_date[0:2])
        month = int(usr_date[3:5])
        year = int(usr_date[6:10])
        return f'День - {day}\nМесяц - {month}\nГод - {year}'

    @staticmethod
    def valid_date(usr_date):
        try:
            day = int(usr_date[0:2])
            month = int(usr_date[3:5])
            year = int(usr_date[6:10])
            date(int(year), int(month), int(day))
            return 'Есть такая дата!'
        except ValueError:
            return 'Такой даты не существует в григорианском календаре!'
        
print(Date.valid_date('29.02.2023'))
print(Date.get_dmy('14.03.2023'))
