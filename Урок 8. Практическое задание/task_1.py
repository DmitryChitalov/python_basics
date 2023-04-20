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
    day_month_year = 'dd-mm-YYYY'

    @classmethod
    def create_attributes(cls):
        cls.day = int(cls.day_month_year[:2])
        cls.month = int(cls.day_month_year[3:5])
        cls.year = int(cls.day_month_year[6:])

    @staticmethod
    def validation_date(day=-1, month=-1, year=-1):
        try:
            if year > 0:
                if month == 2 and year % 4 == 0:
                    if day >= 1 and day <= 29:
                        return True
                    else:
                        return False
                elif month == 2 and year % 4 != 0:
                    if day >= 1 and day <= 28:
                        return True
                    else:
                        return False
                elif month >= 1 and month <= 7 and day >= 1 and day <= 30 + month % 2:
                    return True
                elif month >= 8 and month <= 12 and day >= 1 and day <= 31 - month % 2:
                    return True
                else:
                    return False
            else:
                return False
        except TypeError:
            return False
        except ValueError:
            return False


d = Date()

Date.day_month_year = '31-02-2023'
Date.create_attributes()
print(f"{d.day} {d.month} {d.year} - {Date.validation_date(day=d.day, month=d.month, year=d.year)}")

Date.day_month_year = '31-04-2023'
Date.create_attributes()
print(f"{d.day} {d.month} {d.year} - {Date.validation_date(day=d.day, month=d.month, year=d.year)}")

Date.day_month_year = '31-05-2023'
Date.create_attributes()
print(f"{d.day} {d.month} {d.year} - {Date.validation_date(day=d.day, month=d.month, year=d.year)}")

Date.day_month_year = '29-02-2024'
Date.create_attributes()
print(f"{d.day} {d.month} {d.year} - {Date.validation_date(day=d.day, month=d.month, year=d.year)}")
