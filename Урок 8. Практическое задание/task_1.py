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
class Date:#класс Дата"
    day_month_year = '' #атрибут класса


    @classmethod# Метод класса для извлечения даты и делаем тип число
    def extr_date(cls, date_string):
        date_list = date_string.split('.')
        cls.day_month_year = [int(date_list[0]), int(date_list[1]), int(date_list[2])]


    @staticmethod # Метод статического класса для валидации даты
    def valid_date(day, month, year):
        if 1 <= month <= 12:
            if month in [1, 3, 5, 7, 8, 10, 12]:  # месяц где 31 день
                if 1 <= day <= 31:
                    return True
                else:
                    return False
            elif month in [4, 6, 9, 11]: # месяц где 30 дней
                if 1 <= day <= 30:
                    return True
                else:
                    return False
            else:
                if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0: # высокосный год
                    if 1 <= day <= 29: #для февраля
                        return True
                    else:
                        return False
                else:
                    if 1 <= day <= 28:#для февраля
                        return True
                    else:
                        return False
        else:
            return False


Date.extr_date('15.05.2022') # Извлекаем дату и присваиваем атрибутам класса
print(Date.day_month_year) # Выводим значение атрибута класса

print(Date.valid_date(15, 2, 2022)) # Проверяем валидность даты
print(Date.valid_date(31, 4, 2021)) # Проверяем валидность даты
print(Date.valid_date(25, 3, 2022)) # Проверяем валидность даты
print(Date.valid_date(35, 5, 2022)) # Проверяем валидность даты