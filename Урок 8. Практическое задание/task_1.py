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
    date_string: str

    def __init__(self, date_string):
        self.date_string = date_string

    @classmethod
    def transform(cls, date_string):
        datepart = date_string.split('-')
        return [int(datepart[0]), int(datepart[1]), int(datepart[2])]

    @staticmethod
    def valid(int_string):
        if int_string[1] > 12 or int_string[1] < 1:
            return f"Неверно введены данные. Номер месяца не может быть больше 12 и меньше 1."
        elif int_string[0] < 1:
            return f"Неверно введены данные. Номер дня не может быть меньше 1."
        elif int_string[1] in [1, 3, 5, 7, 8, 10, 12]:
            if int_string[0] > 31:
                return f"Неверно введены данные. В месяце с номером {int_string[1]} должно быть меньше 31 дня"
            else:
                return f"Дата введена верно"
        elif int_string[1] in [4, 6, 9, 11]:
            if int_string[0] > 30:
                return f"Неверно введены данные. В месяце {int_string[1]} должно быть меньше 30 дней"
            else:
                return f"Дата введена верно"
        else:
            if int_string[2] % 4 == 0:
                if int_string[0] > 29:
                    return f"Неверно введены данные. В феврале високосного года не может быть больше 29 дней"
                else:
                    return f"Дата введена верно"
            else:
                if int_string[0] > 28:
                    return f"Неверно введены данные. В феврале невисокосного года не может быть больше 28 дней"
                else:
                    return f"Дата введена верно"


example_string = "32-03-2023"

print(Date.valid(Date.transform(example_string)))
print(Date.valid(Date.transform('01-01-1970')))
