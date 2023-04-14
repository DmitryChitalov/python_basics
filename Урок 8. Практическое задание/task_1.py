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
    day_month_year = " "

    @classmethod
    def input_date(self, date):
        day, month, year = map(int, date.split("."))
        self.day_month_year = (day, month, year)

    @staticmethod
    def date_validation(date):
        day, month, year = map(int, date.split('.'))
        if 0 <= year and 0 < month < 13 and 0 < day < 32:

            if year % 4 == 0:
                if month == 2:
                    if day < 30:
                        print("Дата верна.")
                    else:
                        print("Невозможная дата.")

            elif month == 2:
                if day < 29:
                    print("Дата верна.")
                else:
                    print("Невозможная дата.")
            elif year % 4 != 0 and month != 2:
                print("Дата верна.")

        else:
            print("Невозможная дата.")


intput_to_check = ["31.12.2022", "11.04.2023", "11.04.-2023", "11.14.2023", "-3.14.2023", "29.02.2023"]

for i in intput_to_check:
    print(f"\nПроверяем дату: {i}")
    Date.date_validation(i)
