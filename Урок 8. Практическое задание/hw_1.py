class Date:

    @classmethod
    def my_method(self, dmy):
        d = dmy.split("-")
        self.day, self.month, self.year = dmy.split("-")

    @staticmethod
    def valid():
        if 1 <= int(Date.day) <= 31:
            if 1 <= int(Date.month) <= 12:
                if 2023 >= int(Date.year) >= 0:
                    return f'Правильная дата'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

d = Date()
d.my_method('31-12-2023')
print(d.valid())