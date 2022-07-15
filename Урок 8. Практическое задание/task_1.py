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
    dmy = '01-01-1970'
    day: int
    month: int
    year: int

    @classmethod
    def class_method(cls, *dmy):
        if len(dmy) > 0:
            cls.dmy = dmy[0]
        my_list = cls.dmy.split('-')
        cls.day = int(my_list[0])
        cls.month = int(my_list[1])
        cls.year = int(my_list[2])
        return cls.day, cls.month, cls.year

    @staticmethod
    def static_method(dmy):
        my_list = dmy.split('-')
        result = 'Валидация прошла успешно'
        if not my_list[0].isdigit() or not my_list[1].isdigit() or not my_list[1].isdigit():
            result = 'Введенные данные не являются числами'
        if int(my_list[0]) not in range(1, 32):
            result = 'Значение дня находится за пределами нормальных значений'
        if int(my_list[1]) not in range(1, 13):
            result = 'Значение месяца находится за пределами нормальных значений'
        return result


print(f'Data.class_method() {Data.class_method()}')
print(Data.static_method('01-13-1970'))
my_data1 = Data()
print(my_data1.class_method('11-12-2022'), my_data1.static_method('11-12-2022'))
print(my_data1.static_method('32-01-2022'))
print(my_data1.class_method('33-12-2022'))
