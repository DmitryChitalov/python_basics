from datetime import datetime

class Data:

    data = ""

    @classmethod
    def init(cls):
        buffer = ""
        data_list = []
        for el in range(len(cls.data)):
            if cls.data[el] != "-":
                buffer += cls.data[el]
            else:
                data_list.append(int(buffer))
                buffer = ""
        data_list.append(int(buffer))
        cls.day, cls.month, cls.year = data_list

    @staticmethod
    def valid():
        current_data = datetime.today()
        if current_data.year == Data.year:
            print("Год верный!")
            if current_data.month == Data.month:
                print("Месяц верный!")
                if current_data.day == Data.day:
                    print("День верный")
                else:
                    print(f"Неверный день! Сегодня: {current_data.day}")
            else:
                print(f"Неверный месяц! Сейчас: {current_data.month}")
        else:
            print(f"Неверный год! Сейчас: {current_data.year}")


a = Data
a.data = input("Введите текущую дату в формате 26-11-2022: ")
a.init()
print(a.day, a.month, type(a.year))
print(a.valid())

