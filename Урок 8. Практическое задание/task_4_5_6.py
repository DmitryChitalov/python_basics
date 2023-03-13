"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над четвертым заданием.
Разработать методы, отвечающие за приём оргтехники на
склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над пятым заданием. Р
еализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class Stock:
    # Перечень комнат и принтеров в них
    rooms = {'reseption': {}, 'floor1': {}, 'floor2': {}, 'CEO': {}, 'IT': {}}

    def __init__(self):
        self.availability = dict()

    # Метод который добавляет принтер в какую-то комнату, предварительно проверяя quantity - число?
    def equipment_accounting(self, equip, quantity, room='IT'):
        try:
            if not str(quantity).isdigit():
                raise MyExcept('Вы ввели не число!')
        except MyExcept as err:
            print(err)
        else:
            for k, v in self.rooms.items():
                if k == room:
                    if equip not in v:
                        v[equip] = quantity
                    else:
                        v[equip] += quantity


class OfficeEquipment:
    def __init__(self, name, price, year, model):
        self.name = name
        self.price = price
        self.year = year
        self.model = model

    def info(self):
        print(f'Имя - {self.name}, Цена покупки - {self.price}, Год покупки - {self.year}')


class Printer(OfficeEquipment):
    type = 'Printer'

    def __init__(self, name, price, year, model, color, speed):
        super().__init__(name, price, year, model)
        self.color = color
        self.speed = speed

    def info(self):
        print(f'Имя - {self.name}, Цена покупки - {self.price}, Год покупки - {self.year}, '
              f'Цветность - {"Цветной" if self.color > 1 else "Ч-Б"}')


class Scaner(OfficeEquipment):
    def __init__(self, name, price, year, model, paper_size, speed):
        super().__init__(name, price, year, model)
        self.paper_size = paper_size
        self.speed = speed


class Copier(OfficeEquipment):
    def __init__(self, name, price, year, model, paper_size, walltage):
        super().__init__(name, price, year, model)
        self.paper_size = paper_size
        self.walltage = walltage


class MyExcept(Exception):
    def __init__(self, txt):
        self.txt = txt


my_stock = Stock()
print(my_stock.rooms)
printer1 = Printer('Kyocera M6230', 98200, 2018, 'KyoceraM6230', 4, 35)
printer2 = Printer('Xerox WC 6515', 87000, 2020, 'Xerox WorkCentre 6515DN MFP', 4, 30)
printer3 = Printer('HP 1450', 22000, 2015, 'HP LaserJet 1450REE', 1, 30)
scaner1 = Scaner('Xerox 1632', 15300, 2018, 'Xerox Scan 1632HYD', 4, 35)

my_stock.equipment_accounting(printer1.name, 1, 'reseption')
my_stock.equipment_accounting(printer2.name, 3, 'floor1')
my_stock.equipment_accounting(printer3.name, 2, 'reseption')
my_stock.equipment_accounting(scaner1.name, 1, 'CEO')
my_stock.equipment_accounting(scaner1.name, 'q')
my_stock.equipment_accounting(printer1.name, 2)

printer1.info()
printer2.info()
scaner1.info()

print(my_stock.rooms)
