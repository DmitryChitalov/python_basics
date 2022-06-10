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

class DateError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


class Date:

    def __init__(self, str_val):
        self.__date_str = str_val
        self.__date_list = self.convert_to_int(str_val)
        self.check_values(list(self.__date_list))

    @classmethod
    def convert_to_int(cls, str_val):
        return [val for val in map(int, str_val.split('-'))]

    @staticmethod
    def check_values(val: list):
        leap_year = (not val[2] % 400) or (val[2] % 100 and (
            not val[2] % 4))
        if not (0 < val[1] <= 12):
            raise DateError(f'Violated the number of months in a year (12)')
        days_in_month = \
        (31, 29 if leap_year else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)[
            val[1] - 1]
        if not (0 < val[0] <= days_in_month):
            raise DateError(
                f'Violated the number of days in a month ({days_in_month})')


if __name__ == '__main__':
    d = Date('20-06-2022')
