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


class DateClass:
    """Свой класс Даты"""
    day_month_year = '22-12-2022'

    @classmethod
    def create_date(cls):
        '''Метод класса'''
        new_day = cls.day_month_year.split('-')
        cls.day = int(new_day[0])
        cls.month = int(new_day[1])
        cls.year = int(new_day[2])

    @staticmethod
    def validate():
        """Валидация данных"""
        if DateClass.day >= 1 and DateClass.day <= 31:
            if DateClass.month >= 1 and DateClass.month <= 12:
                if DateClass.year <= 2022:
                    print(f"Дата {DateClass.day}.{DateClass.month}.{DateClass.year} - нормальная")
                else:
                    print(f'Год {DateClass.year} некорректный')
            else:
                print(f'Месяц {DateClass.month} некорректный')
        else:
            print(f'День {DateClass.day} некорректный')


DateClass.create_date()
DateClass.validate()
