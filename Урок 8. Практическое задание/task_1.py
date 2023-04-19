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
    day_month_year = '2023-04-18'

    @classmethod
    def make_attributes(cls):
        cls.year = int(cls.day_month_year.split('-')[0])
        cls.month = int(cls.day_month_year.split('-')[1])
        cls.day = int(cls.day_month_year.split('-')[2])

    @staticmethod
    def validator(date):
        messages = 'Validation result: \n'
        try:
            year = int(date.split('-')[0])
            month = int(date.split('-')[1])
            day = int(date.split('-')[2])
        except:
            messages += 'Date is not valid \n'
            return messages
        if month not in range(1, 13):
            messages += 'Not valid month \n'
        else:
            messages += 'Month is ok \n'
        if day not in range(1,32):
            messages += 'Not valid day \n'
        else:
            messages += 'Day is ok \n'
        return messages





d = Date()
d.make_attributes()
print(d.day_month_year)
print(d.year)
print(d.month)
print(d.day)

print(Date().year)
print(Date().month)
print(Date().day)

print(Date().validator('2023-01-30'))
print(Date().validator('2023-25-30'))
print(Date().validator('sgn-25-30'))