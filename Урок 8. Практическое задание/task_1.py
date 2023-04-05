class Data:
    day_month_year = "4 - 4 - 2023"

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != "-": my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 9999:
                    return f"Все введено правильно"
                else:
                    return f"Неправильные данные"
            else:
                return f"Неправильные данные"
        else:
            return f"Неправильные данные"


a = Data

print(Data.valid(44, 4, 2023))
print(Data.valid(4, 4, 2023))
print(Data.extract("4 - 4 - 2023"))
