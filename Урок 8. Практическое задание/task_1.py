class Data:

    def __init__(self, a):
        self.day_month_year = "4 - 4 - 2023"

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != "-": my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 9999:
                    return f"Все введено правильно"
                else:
                    return f"Неправильные данные"
            else:
                return f"Неправильные данные"
        else:
            return f"Неправильные данные"


print(Data.valid(44, 4, 2023))
print(Data.valid(4, 4, 2023))
print(Data.extract("4 - 4 - 2023"))

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
