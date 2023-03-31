#  Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
#  В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
#  Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
#  Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
#  Проверить работу полученной структуры на реальных данных.
class Date:
    def __init__(self, date_str):
        self.day, self.month, self.year = self.extract_date(date_str)

    @classmethod
    def from_string(cls, date_str):
        return cls(date_str)

    @staticmethod
    def is_valid_date(day, month, year):
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        if month == 2 and day > 29:
            return False
        if month in [4, 6, 9, 11] and day > 30:
            return False
        if year < 0:
            return False
        return day, month, year

    def is_valid(self):
        return self.is_valid_date(self.day, self.month, self.year)

    @staticmethod
    def extract_date(date_str):
        day, month, year = map(int, date_str.split("-"))
        return day, month, year

date_str = "31-12-2022"
date = Date.from_string(date_str)
print(date.is_valid())  # True

date_str = '31-12-2022'
date = Date(date_str)
print(date.day, date.month, date.year)  # 31 12 2022

today = Date('11 - 1 - 2001')
print(Date.is_valid_date(11, 11, 2022)) # True
print(today.is_valid_date(11, 13, 2011)) # False
print(Date.is_valid_date(1, 11, 2000)) # True