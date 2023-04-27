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
    def __init__(self, date):
        self.date = date.split('-')

    @classmethod
    def extract(cls, date):
        date = date.split('-')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
        return day, month, year

    @staticmethod
    def check_date(date):
        day, month, year = Date.extract(date)  # classmethod
        good_date = True

        def bad_date():
            """Переменной good_date присваивается значение False"""
            nonlocal good_date
            good_date = False

        def is_leap_year(year):
            """Возвращение значения високосный ли год"""
            if year % 100 == 0 and year % 400 != 0:
                result = False
            elif year % 400 == 0:
                result = True
            elif year % 4 == 0:
                result = True
            else:
                result = False
            return result

        if month < 1 or month > 12:  # проверка месяца от 1 до 12
            print(f"Значение месяца должно быть от 1 до 12, введено {month}")
            bad_date()
        if month == 2 and is_leap_year(year) and (day > 29 or day < 1):  # проверка даты в феврале високосного года
            print(f"Для месяца {month} введено не верное количество дней {day}")
            bad_date()
        elif month == 2 and (day > 28 or day < 1):  # проверка даты в феврале не високосного года
            print(f"Для месяца {month} введено не верное количество дней {day}")
            bad_date()
        elif month in (1, 3, 5, 7, 8, 10, 12) and (day > 31 or day < 1):  # проверка даты в месяцах, где 31 день
            print(f"Для месяца {month} введено не верное количество дней {day}")
            bad_date()
        elif month in (4, 6, 9, 11) and (day > 30 or day < 1):  # проверка даты в месяцах,где 30 дней
            print(f"Для месяца {month} введено не верное количество дней {day}")
            bad_date()
        if year > 2030 or year < 0:  # проверка года от 0 до 2030
            print(f"Значение года должно быть от 0 до 2050, введено {year}")
            bad_date()
        if good_date:
            print("Введена верная дата")

# проверяем работу 
Date.check_date("25-10-2044")
print()
Date.check_date("31-02-2001")
print()
Date.check_date("31-06-2001")
print()
Date.check_date("21-02-1999")
print()
Date.check_date("29-02-2000")
