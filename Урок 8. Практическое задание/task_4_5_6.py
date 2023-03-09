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

class OfficeEquipmentWarehouse:
    def __init__(self):
        self.product_stock = {}
        self.technique_by_department = {}

    def add_product(self, obj):
        if self.product_stock.get(obj.name):
            self.product_stock[obj.name] += 1
            return self.product_stock
        else:
           return self.product_stock.update({obj.name: 1})
        
    def transfer_equipment(self, department, product, quantity):
        self.technique_by_department.update({department: [product, quantity]})
        self.product_stock[product] = self.product_stock[product] - quantity
        return self.technique_by_department
            
    def __str__(self):
        return f'На складе: {self.product_stock}\nВ подразделениях: {self.technique_by_department}'

class OfficeEquipment:
    def __init__(self, producer):
        self.producer = producer

class Printer(OfficeEquipment):
    def __init__(self, producer, color):
        super().__init__(producer)
        self.name = 'принтер'
        self.color = color

class Scanner(OfficeEquipment):
    def __init__(self, producer, format):
        super().__init__(producer)
        self.name = 'сканер'
        self.format = format

class Xerox(OfficeEquipment):
    def __init__(self, producer, size):
        super().__init__(producer)
        self.name = 'ксерокс'
        self.size = size


class NumberQuantityError(Exception):
    def __init__(self, message):
        self.message = message
        
class ProductNameError(Exception):
    def __init__(self, message):
        self.message = message

office_equipment_warehouse = OfficeEquipmentWarehouse()
printer_1 = Printer('canon', 'red')
printer_2 = Printer('sony', 'blue')
scanner_1 = Scanner('canon', 'A4')
xerox_1 = Xerox('xerox', 'small')

office_equipment_warehouse.add_product(printer_1)
office_equipment_warehouse.add_product(printer_2)
office_equipment_warehouse.add_product(scanner_1)
office_equipment_warehouse.add_product(xerox_1)

print(office_equipment_warehouse)

try:
    department = input('Введите название департамента: ')
    product = input('Введите название продукта: ')
    quantity = int(input('Введите количество продукта: '))
    
    if office_equipment_warehouse.product_stock.get(product) == None:
        raise ProductNameError("Продукт на складе отсутствует.")
    
    if quantity < 1 or quantity > office_equipment_warehouse.product_stock[product]:
        raise NumberQuantityError('Некорректное количество.')
    
    office_equipment_warehouse.transfer_equipment(department, product, quantity)
    print(office_equipment_warehouse)
    
except ValueError:
    print('Не число!')
    
except ProductNameError as e:
    print(e)
    
except NumberQuantityError as e:
    print(e)
        
