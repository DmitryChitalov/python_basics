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

class EquipmentClassError(Exception):
    def __str__(self):
        return 'Wrong equipment class'

class Warehouse:
    goods = {'printers': [], 'skanners': [], 'xeroxes': []}

    @staticmethod
    def check_class(equipment):
        try:
            if equipment.__class__.__name__ in ['Printer', 'Skanner', 'Xerox']:
                return 1
            else:
                raise EquipmentClassError
        except EquipmentClassError as err:
            print(f'{err}: {equipment.__class__.__name__}')

    @classmethod
    def receive(cls, equipment):
        if cls.check_class(equipment):
            if equipment.__class__.__name__ == 'Printer':
                cls.goods['printers'].append(equipment)
            if equipment.__class__.__name__ == 'Skanner':
                cls.goods['skanners'].append(equipment)
            if equipment.__class__.__name__ == 'Xerox':
                cls.goods['xeroxes'].append(equipment)
    
    @classmethod
    def give(cls, equipment):
        if cls.check_class(equipment):
            if equipment.__class__.__name__ == 'Printer':
                cls.goods['printers'].pop()
            if equipment.__class__.__name__ == 'Skanner':
                cls.goods['skanners'].pop()
            if equipment.__class__.__name__ == 'Xerox':
                cls.goods['xeroxes'].pop()

class OfficeEquipment:
    material = 'Plastic'

class Printer(OfficeEquipment):
    def __init__(self, pages_per_minute):
        self.pages_per_minute = pages_per_minute

class Skanner(OfficeEquipment):
    def __init__(self, paper_size):
        self.paper_size = paper_size

class Xerox(OfficeEquipment):
    def __init__(self, white_n_black_only):
        self.white_n_black_only = white_n_black_only

p = Printer(10)
s= Skanner('A3')
x = Xerox(False)
g = 1

Warehouse.receive(p)
Warehouse.receive(s)
Warehouse.receive(x)
Warehouse.receive(g)

Warehouse.give(s)

print(f'На складе {len(Warehouse.goods["printers"])} принтеров, {len(Warehouse.goods["skanners"])} сканеров, {len(Warehouse.goods["xeroxes"])} ксероксов')

