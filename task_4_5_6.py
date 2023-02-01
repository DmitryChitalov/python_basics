class Stock:
    def __init__(self):
        self.tech_dict = {}
        self.full_dict = {}

    def account(self, type, number):
        self.tech_dict.update({type: number})

    def full_account(self, type, data):
        self.full_dict.update({type: data})


class Technics:
    def __init__(self, name, year, producer):
        self.name = name
        self.year = year
        self.producer = producer

class Printer(Technics):
    def __init__(self, name, year, producer, technology):
        super().__init__(name, year, producer)
        self.technology = technology
        self.colors = colors

class Scanner(Technics):
    def __init__(self, name, year, producer, format):
        super().__init__(name, year, producer)
        self.format = format

class Xerox(Technics):
    def __init__(self, name, year, producer, size):
        super().__init__(name, year, producer)
        self.size = size

class TechError(Exception):
    def __init__(self, txt):
        self.txt = txt

class NumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

st = Stock()
while True:
    try:
        type = input("Укажите тип оборудования (принтер, сканер или ксерокс). "
                 "Для выхода из программы введите q. ")
        if type == 'q':
            print(st.tech_dict)
            print(st.full_dict)
            break
        number = input("Укажите число экземпляров: ")
        if number.isdigit() == False:
            raise NumberError("Вы ввели не число!")
            continue
        st.account(type, number)
        if type == 'принтер':
            for el in range(1, (int(number) + 1)):
                data = input("Введите характеристики принтера "
                         "через пробел(фирма, год выпуска, производитель, "
                         "технология печати: ").split()
                st.full_account(type, data)
        elif type == 'сканер':
            for el in range(1, (int(number) + 1)):
                data = input("Введите характеристики сканера "
                         "через пробел(фирма, год выпуска, производитель, "
                         "формат сканирования: ").split()
                st.full_account(type, data)
        elif type == 'ксерокс':
            for el in range(1, (int(number) + 1)):
                data = input("Введите характеристики ксерокса "
                         "через пробел(фирма, год выпуска, производитель, "
                         "размер листа: ").split()
                st.full_account(type, data)
        else:
            raise TechError("Вы неверно указали тип оборудования!")
            continue
    except TechError as err:
        print(err)
    except NumberError as err:
        print(err)