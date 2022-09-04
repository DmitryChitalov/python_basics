class Date:
    def __int__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def my_method_1(cls, day_month_year):
        my_date = []

        for el in day_month_year.split('_'):
            my_date.append(el)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid_date(day, month, year):
        if 1 <= day <= 31 and 1 <= month <= 12:
            return day, month, year
        else:
            print("Ошибка")

    def __str__(self):
        return Date.my_method_1(self.day_month_year)


d = Date()
print(d.my_method_1('04_09_2022'))
print(d.valid_date(4, 9, 2022))
