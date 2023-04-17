"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число».

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

class Data:
   
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    def __str__(self):
        return f'Введенная дата {Data.data_extraction(self.day_month_year)}'
    
    @classmethod
    def data_extraction(cls, day_month_year):
        my_list = []
        my_data = day_month_year.split()

        for i in my_data:
            if i != '-': 
                my_list.append(int(i))

        return my_list[0], my_list[1], my_list[2]

    @staticmethod
    def validation(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if year >= 0:
                    return f'Введенные данные корректны'
                else:
                    return f'Год должен быть задан неотрицательным числом'
            else:
                return f'Месяц должен быть задан в диапазоне от 1 до 12'
        else:
            return f'День должен быть задан в диапазоне от 1 до 31'

    
obj_data = Data('16 - 7 - 1995')
print(obj_data)
print(obj_data.validation(0, 12, 3022))
print(Data.data_extraction('25 - 0 - 1980'))
print(Data.validation(25, 100, 1968))
