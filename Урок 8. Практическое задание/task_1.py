"""
Задание 1.

Реализовать класс «Дата», конструктор которого должен принимать дату
в виде строки формата «день-месяц-год».

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число».

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:

    day_month_year = "11 - 1 - 2020"

    @classmethod
    def extract(cls):
        my_date = [int(el) for el in cls.day_month_year.split() if el != '-']
        cls.day, cls.month, cls.year = my_date

    @staticmethod
    def valid():

        if 1 <= Data.day <= 31:
            if 1 <= Data.month <= 12:
                if 2020 >= Data.year >= 0:
                    return f"Все в порядке"
                else:
                    return f"Неправильный год"
            else:
                return f"Неправильный месяц"
        else:
            return f"Неправильный день"


Data.extract()
print(Data.valid())
