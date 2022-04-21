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

from time import strptime

class Data:
    date: str

    def __init__(self, curr_data: str):
        self.date = curr_data

    @classmethod
    def set_digit(cls, content: str):
        tmp_list = list(map(int, content.date.split("-")))
        return tmp_list


    @staticmethod
    def validate_data(inp_data: str):
        is_correct = False
        try:
            valid_date = strptime(inp_data, '%d-%m-%Y')
            is_correct = True
        except ValueError:
            is_correct = False

        return is_correct


my_data = "23-06-2021"

if Data.validate_data(my_data):
    my_data_element = Data(my_data)
    print(Data.set_digit(my_data_element))
else:
    print("Неправильный формат даты")
