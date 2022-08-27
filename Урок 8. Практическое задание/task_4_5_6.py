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

class WareHouse:
    '''Склад'''
    pass

class OfficeEquipment(ABC):
    '''оргтехника'''
    def __init__(self, brand, model,
    inv_number):
        self.brand = brand
        self.model = model
        self.inv_number = inv_number

class Printer(OfficeEquipment):
    '''принтер'''
    def __init__(self, brand, model,
    inv_number, dev_type, print_type, print_speed):
        self.dev_type = dev_type
        self.print_type = print_type
        self.print_speed = print_speed
        super().__init__(brand, model, inv_number)

class Scanner(OfficeEquipment):
    '''сканер'''
    def __init__(self, brand, model, inv_number,
    scan_type, max_letter_type, max_dpi):
        self.scan_type = scan_type
        self.max_letter_type = max_letter_type
        self.max_dpi = max_dpi
        super().__init__(brand, model, inv_number)

class Xerox(Printer, Scanner):
    '''ксерокс'''
    def __init__(self, brand, model, inv_number, dev_type, print_type,
    print_speed,scan_type, max_letter_type, max_dpi):
        self.brand = brand
        self.model = model
        self.inv_number = inv_number
        self.dev_type = dev_type
        self.print_type = print_type
        self.print_speed = print_speed
        self.scan_type = scan_type
        self.max_letter_type = max_letter_type
        self.max_dpi = max_dpi


xer_1 = Xerox('brand','model', 12344,'dev_type',
'print_type', 'print_speed', 'scan_type', 'max_letter_type', 'max_dpi')

print(xer_1.__dict__)
