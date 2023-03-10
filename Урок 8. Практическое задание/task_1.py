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
class MyDate:
    year_month_day = '1970-41-01'

    @classmethod
    def make_atr(self, year_month_day):
        self.year_month_day = year_month_day
        self.year = int(self.year_month_day[0:4])
        self.month = int(self.year_month_day[5:7])
        self.day = int(self.year_month_day[8:10])
        return self.year, self.month, self.day

    @staticmethod
    def validation(self):
        try:
            day, month, year = self.year_month_day.split('-')
            date(int(year), int(month), int(day))
            return 'Дата существует'
        except ValueError:
            return 'Вы указали неправильный формат даты'

a = MyDate
a.make_atr(a.year_month_day)
print(a.year)
print(a.month)
print(a.day)
print(a.validation(a))