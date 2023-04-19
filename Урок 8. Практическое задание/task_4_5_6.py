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

6. Продолжить работу над пятым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
from abc import ABC, abstractmethod


class OfficeEquipment(ABC):
    name: str
    quantity: int

    @abstractmethod
    def to_warehouse(self, whs):
        pass


class Printer(OfficeEquipment, ABC):
    def __init__(self, name, print_color):
        self.name = name
        self.print_color = print_color

    def to_warehouse(self, whs):
        whs.data.update({self.__class__.__name__: whs.data[self.__class__.__name__] + 1 })


class Scaner(OfficeEquipment, ABC):
    def __init__(self, name, memory_limit):
        self.name = name
        self.memory_limit = memory_limit

    def to_warehouse(self, whs):
        whs.data.update({self.__class__.__name__: whs.data[self.__class__.__name__] + 1 })


class Xerox(OfficeEquipment, ABC):
    def __init__(self, name, paper_format):
        self.name = name
        self.paper_format = paper_format

    def to_warehouse(self, whs):
        whs.data.update({self.__class__.__name__: whs.data[self.__class__.__name__] + 1 })


class Warehouse:
    data = {'Printer': 0,
            'Scaner': 0,
            'Xerox': 0}

    @classmethod
    def to_department(cls, equipment, quantity):
        try:
            cls.data[equipment] -= quantity
        except:
            print('Quantity has to be integer')


printer_1 = Printer('Printer_1', 'rgb')
print(printer_1.name)
print(printer_1.print_color)

scaner_1 = Scaner('Scaner_1', '8G')
print(scaner_1.name)
print(scaner_1.memory_limit)

xerox_1 = Xerox('Xerox_1', 'A4')
print(xerox_1.name)
print(xerox_1.paper_format)

warehouse = Warehouse()

printer_1.to_warehouse(warehouse)
scaner_1.to_warehouse(warehouse)
xerox_1.to_warehouse(warehouse)
print(warehouse.data)

warehouse.to_department('Printer', 1)
print(warehouse.data)

warehouse.to_department('Xerox', '1')