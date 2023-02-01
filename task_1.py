class Date:
    def __init__(self, param):
        self.param = param


    @classmethod
    def my_method_1(cls, param):
        date_list = param.split('-')
        for el in date_list:
            el = int(el)
        day = date_list[0]
        month = date_list[1]
        year = date_list[2]
        print(f"День - {day}, месяц - {month}, год - {year}")
        return Date.my_method_2(day, month, year)

    @staticmethod
    def my_method_2(day, month, year):
        if int(month) < 1 or int(month) > 12:
            print("Вы ввели неверное значение месяца")
        if int(day) < 1 or int(day) > 31:
            print("Вы ввели неверное значение дня")
        if int(month) == 2 and int(day) > 28:
            print("Вы ввели неверное значение дня")

new_date = input("Введите дату в формате день-месяц-год: ")
Date.my_method_1(new_date)