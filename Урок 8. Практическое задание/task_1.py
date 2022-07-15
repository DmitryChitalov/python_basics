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
    day_month_year = ""

    @classmethod
    def get_int_values(cls):
        try:
            print(Date.day_month_year.split('-'))
        except BaseException as e:
            print(f"Errors: {e}")

    @staticmethod
    def validate_data():
        try:
            __errors = []
            __year = int(Date.day_month_year.split('-')[2])
            __month = int(Date.day_month_year.split('-')[1])
            __day = int(Date.day_month_year.split('-')[0])
            _days = -1

            if __year < 1000:
                __errors.append(f"Некорректный формат года: [{__year}]")

            if __month < 1 or __month > 12:
                __errors.append(f"Некорректный формат месяца: [{__month}]")

            if __month == 1 \
                    or __month == 3 \
                    or __month == 5 \
                    or __month == 7 \
                    or __month == 8 \
                    or __month == 10 \
                    or __month == 12:
                _days = 31
            elif __month == 4 \
                    or __month == 6 \
                    or __month == 9 \
                    or __month == 11:
                _days = 30
            elif __year % 4 == 0 and __year % 100 != 0 or __year % 400 == 0:
                _days = 29
            else:
                __days = 28

            if (__day > _days or __day < 1) and len(__errors) == 0:
                print(f"Некорретное число дней в месяце: [{__day}]")

            if len(__errors) > 0:
                print("Ошибки при проверке даты:")
                for el in __errors:
                    print(el)
            else:
                print(f"Формат даты корректный: {Date.day_month_year}")

        except BaseException as e:
            print(f"Error: {e}")


Date.day_month_year = "31-11-2022"
Date.validate_data()
Date.get_int_values()

