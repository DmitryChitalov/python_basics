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
    day_month_year = "22-11-2017"

    @classmethod
    def date_extract(cls):
        tmp_list = Date.day_month_year.split("-")
        Date.date_day = int(tmp_list[0])
        Date.date_mnth = int(tmp_list[1])
        Date.date_year = int(tmp_list[2])
        print(Date.date_day)
        print(Date.date_mnth)
        print(Date.date_year)

    @staticmethod
    def date_validate(in_date):
        date_dict = {"1": 31, "2": 29, "3": 31, "4": 30, "5": 31, "6": 30, "7": 31, "8": 31, "9": 30, "10": 31}
        tmp_dict = {"11": 30, "12": 31}
        date_dict.update(tmp_dict)
        tmp_list = in_date.split("-")
        try:
            d_day = int(tmp_list[0])
            d_mnth = int(tmp_list[1])
            d_year = int(tmp_list[2])
        except ValueError:
            print("Не соблюден формат ввода даты")
            return

        if d_mnth > 12 or d_mnth < 1:
            print("Введен недопустимый месяц")
        else:
            if d_day > date_dict.get(str(d_mnth)):
                print("Введен недопустимый день месяца")
            elif d_year > 2100 or d_year < 1000:
                print("Возможно некорректно введен год")
            else:
                print("Ошибки не обнаружены")


inp_date = input("Введите дату в формате дд-мм-гггг: ")
Date.date_validate(inp_date)
print()
Date.date_extract()
print()
Date.day_month_year = "12-03-2020"
Date.date_extract()
