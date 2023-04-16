class Date:
    day_month_year = None

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_string):
        day, month, year = map(int, date_string.split("-"))
        cls.day_month_year = (day, month, year)
        return cls(day, month, year)

    @staticmethod
    def is_valid(day, month, year):
        if not 1 <= month <= 12:
            return False
        if month in {4, 6, 9, 11} and not 1 <= day <= 30:
            return False
        if month == 2 and not (1 <= day <= 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 1 <= day <= 28):
            return False
        if not 1 <= day <= 31:
            return False
        return True


date_string = "13-03-2023"
date = Date.from_string(date_string)

if Date.is_valid(date.day, date.month, date.year):
    print("Дата корректна")
else:
    print("Дата некорректна")
