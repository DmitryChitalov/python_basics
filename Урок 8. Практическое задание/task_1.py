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
class Data:
    def __init__(self, dates):
        self.dates = str(dates)

    @classmethod
    def date_list(cls, dates):
        my_date = []

        for i in dates.split():
            if i != "-":
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if year == 2023:
            if 1 <= month <= 12:
                if 0 < day <= 31:
                    return "Continue"
                else:
                    return "Wrong day"
            else:
                return "Wrong month"
        else:
            return "Wrong year"

    def __str__(self):
        return f"Today is {Data.date_list(self.dates)}"


today = Data("11 - 4 - 2023")
print(today)
print(Data.valid(11, 1, 2022))
print(today.valid(11, 13, 2023))
print(Data.date_list("11 - 11 - 2011"))
