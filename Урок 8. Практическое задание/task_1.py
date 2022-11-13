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
class BadDate(Exception):
    def __init__(self, txt):
        self.txt = txt


class MyDate:
    day_month_year = ''
    day = 0
    month = 0
    year = 0

    def __init__(self, date_str):
        self.day_month_year = date_str  # format: 'DD.MM.YYYY'
        return

    @classmethod
    def set_day_mon_year(cls, arg1):
        lst = arg1.split('.', maxsplit=2)
        nd = int(lst[0])
        nm = int(lst[1])
        ny = int(lst[2])
        cls.validate_params(nd, nm, ny)
        cls.day = nd
        cls.month = nm
        cls.year = ny
        return

    @staticmethod
    def validate_params(n_day, n_month, n_year):
        try:
            if n_year < 0:
                raise BadDate('Неверный год!')
            elif n_month < 1 or n_month > 12:
                raise BadDate('Неверный месяц!')
            elif n_day < 1 or n_day > 31:
                raise BadDate('Неверный день!')
        except BadDate as err:
            print(err)
            return -1
        return 0

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"


s_date = input("введите дату в формате ДД.ММ.ГГГГ :")
MyDate.set_day_mon_year(s_date)
obj = MyDate("01.01.1901")
MyDate.set_day_mon_year(s_date)
print(obj)                  # выводит введенную пользователем дату
