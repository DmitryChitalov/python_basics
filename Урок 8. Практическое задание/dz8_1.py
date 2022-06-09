#  Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
#  В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
#  преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
#  и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

import re


class MyDate():
    def __init__(self, datestr):
        yearnum, monthnum, daynum = self.parse_datestr(datestr)
        if MyDate.verify_ymd(yearnum, monthnum, daynum):
            self.yearnum = yearnum
            self.monthnum = monthnum
            self.daynum = daynum

    def __str__(self):
        return "Корректная дата: %04d-%02d-%02d" % (self.yearnum, self.monthnum, self.daynum)

    @classmethod
    def parse_datestr(cls, datestr):
        match = re.match(r'(\d{4})-(\d{2})-(\d{2})', datestr)
        if match:
            return int(match.group(1)), int(match.group(2)), int(match.group(3))
        else:
            raise ValueError("Формат даты " + datestr + " не соответствует шаблону ГГГГ-ММ-ДД")

    @staticmethod
    def verify_ymd(yearnum, monthnum, daynum):
        if not (yearnum >= 1000 and yearnum <= 2999):
            raise ValueError("неверный год в дате: " + str(yearnum))
        if not (monthnum >= 1 and monthnum <= 12):
            raise ValueError("неверный месяц в дате: " + str(monthnum))
        if not (daynum >= 1 and daynum <= 31):
            raise ValueError("неверный день в дате: " + str(daynum))
        return True


# примеры дат и их проверка
try:
    d = MyDate('2022-ff-xxxx')
    print(d)
except Exception as e:
    print(e)

try:
    d = MyDate('4651-01-01')
    print(d)
except Exception as e:
    print(e)

try:
    d = MyDate('1862-20-07')
    print(d)
except Exception as e:
    print(e)

try:
    d = MyDate('1322-12-50')
    print(d)
except Exception as e:
    print(e)

try:
    d = MyDate('1978-12-09')
    print(d)
except Exception as e:
    print(e)
