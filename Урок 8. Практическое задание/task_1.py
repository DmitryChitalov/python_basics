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
class MyDate:
    '''Дата'''
    day_month_year = ''

    @classmethod
    def extract(cls):
        '''Экстрактор d_m_y'''
        var_list = cls.day_month_year.split('_')
        processed_list = [int(el) for el in var_list]
        cls.day = processed_list[0]
        cls.month = processed_list[1]
        cls.year = processed_list[2]
    @staticmethod
    def validate(day, month, year):
        '''валидация данных'''
        valid_day = False
        valid_month = False
        valid_year = False
        if day > 0 & day < 32:
            valid_day = True
        if month > 0 & month < 13:
            valid_month = True
        if year > 0 and year < 3000:
            valid_year = True
        return valid_day, valid_month, valid_year

test = MyDate
test.day_month_year = '01_05_2022'
test.extract()
print(test.validate(test.day,test.month, test.year))
