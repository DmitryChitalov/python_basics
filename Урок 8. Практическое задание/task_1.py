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

# Выводим на экран задание
print('\nУрок 8 Задание 1\n')

# Создаем класс
class DateCheck:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extr_date(cls, day_month_year):
        date_list = list(day_month_year.split('.'))
        DateCheck.day = int(date_list[0])
        DateCheck.month = int(date_list[1])
        DateCheck.year = int(date_list[2])

    @staticmethod
    def date_check():
        if DateCheck.year > 0 and DateCheck.year <= 2022:
            if DateCheck.month > 0 and DateCheck.month < 13:
                if DateCheck.day > 0 and DateCheck.day < 31:
                    return f'Сегодня {DateCheck.day}.{DateCheck.month}.{DateCheck.year} г.'
                else:
                    print('Такой даты не существует!')
            else:
                print('Такого месяца не существует!')
        else:
            print('Такой год еще не настал!')


# Объявняем переменные и выводим на экран
input_date = input('Введите дату(дд.мм.гггг): ')
DateCheck.extr_date(input_date)
print(DateCheck.date_check())
