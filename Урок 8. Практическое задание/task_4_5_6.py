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
from abc import ABC


class Storage:
    my_storage = {}
    user_storage = {}


class ErrorUser(Exception):
    pass


class OfficeEquipment(ABC):
    name = None
    max_price = 500

    def __init__(self, color, vendor, model, price):
        self.color = color
        self.vendor = vendor
        self.model = model
        self.price = price

    def check_price(self):
        try:
            if self.max_price < self.price:
                raise ErrorUser('Превышен максимальный прайс')
        except ErrorUser as eu:
            print(eu)
        else:
            self.add()

    def add(self):
        var = {'color': self.color, 'vendor': self.vendor, 'model': self.model, 'В наличии': 1}
        if self.name not in Storage.my_storage.keys():
            Storage.my_storage[self.name] = [var]
        else:
            if var in Storage.my_storage[self.name]:
                index_var = Storage.my_storage[self.name].index(var)
                Storage.my_storage[self.name][index_var]['В наличии'] += 1
            else:
                Storage.my_storage[self.name].append(var)
        print(Storage.my_storage[self.name])

    def transfer(self):
        print(self.color, self.vendor, self.model)
        print(Storage.my_storage[self.name])
        for i, el in enumerate(Storage.my_storage[self.name]):
            if el['color'] == self.color and el['vendor'] == self.vendor and el['model'] == self.model:
                if Storage.my_storage[self.name][i]['В наличии'] > 0:
                    Storage.my_storage[self.name][i]['В наличии'] -= 1
                    print('Перемещение произошло успешно!')
                if Storage.my_storage[self.name][i]['В наличии'] == 0:
                    del Storage.my_storage[self.name][i]


class Printer(OfficeEquipment):
    name = 'Принтер'


class Scaner(OfficeEquipment):
    name = 'Сканер'


class Xerox(OfficeEquipment):
    name = 'Ксерокс'


my_xerox = Xerox('Белый', 'Xerox', 'M55', 100)
my_xerox.check_price()
my_xerox2 = Xerox('Черный', 'Xerox', 'M55', 100)
my_xerox2.check_price()
my_xerox3 = Xerox('Черный', 'Xerox', 'M55', 13300)
my_xerox3.check_price()
my_xerox2.transfer()
my_xerox2.transfer()
print(Storage.my_storage)
