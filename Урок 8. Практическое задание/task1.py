class Data:
    day_month_year = "31 - 12 - 2023"

    @classmethod
    def extract(cls):
        my_date = [int(el) for el in cls.day_month_year.split() if el != '-']
        cls.day, cls.month, cls.year = my_date

    @staticmethod
    def valid():
        if 1 <= Data.day <= 31:
            if 1 <= Data.month <= 12:
                if 2023 >= Data.year >= 0:
                    return f"Дата верная"
                else:
                    return f"Неверный год"
            else:
                return f"Неверный месяц"
        else:
            return f"Неверный день"


Data.extract()
print(Data.valid())
