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

    day_month_year = '19-01-2023'

    @classmethod
    def extract_dmy(cls):
        return int(cls.day_month_year.split('-')[0]), int(cls.day_month_year.split('-')[1]), int(cls.day_month_year.split('-')[2])

    @staticmethod
    def is_date_valid(d, m, y):
        dates_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 31, 12: 31}
        if int(y) >= 2022:
            if 12 >= int(m) >= 1:
                if int(y) // 4 == 0 and int(m) == 2:
                    if 1 >= int(d) >= 29:
                        return 'ок'
                    else:
                        return 'некорректно указан день'
                else:
                    if 1 <= int(d) <= dates_dict[int(m)]:
                        return 'ок'
                    else:
                        return 'некорректно указан день'
            else:
                return 'некорректно указан месяц'
        else:
            return 'некорректно указан год'


print(Date.extract_dmy())
print(Date.is_date_valid(28, 2, 2022))
