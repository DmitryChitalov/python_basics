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


class MyDate():
    day_month_year = ""

    @staticmethod
    def validate_date(param=None):
        result = False
        if type(param) == str:
            lst = param.split("_")
            for idx, i in enumerate(lst):
                try:
                    value = int(i);
                    if value <= 0:
                        result = False
                        break
                    elif idx == 0:
                        if value > 31:
                            result = False
                            break
                    elif idx == 1:
                        if value > 12:
                            result = False
                            break
                    result = True
                except ValueError:
                    result = False
                    break
        else:
            print("Некорректный параметр")
        return result

    @classmethod
    def get_attrib(cls):
        lst = cls.day_month_year.split("_")
        for idx, i in enumerate(lst):
            try:
                if idx == 0:
                    setattr(cls, "_day", int(i))
                elif idx == 1:
                    setattr(cls, "_month", int(i))
                elif idx == 2:
                    setattr(cls, "_year", int(i))
            except ValueError:
                print(f"Не удалось преобразовать к дате {cls.day_month_year}")


my_date = MyDate
param1 = "12_12_2022"
if my_date.validate_date(param1):
    my_date.day_month_year = param1
    my_date.get_attrib()
    print(my_date.__dict__)
param1 = "12_31_2022"
if my_date.validate_date(param1):
    my_date.day_month_year = param1
    my_date.get_attrib()
    print(my_date.__dict__)
