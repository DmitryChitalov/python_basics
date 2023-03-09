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

class OfficeEquipment:
    def __init__(self, model, price, year):
        self.model = model
        self.price = price
        self.year = year

    def __str__(self):
        return f"{self.__class__.__name__} {self.model}, price: {self.price}, year: {self.year}"

class Printer(OfficeEquipment):
    def __init__(self, model, price, year, max_print_speed):
        super().__init__(model, price, year)
        self.max_print_speed = max_print_speed

    def __str__(self):
        return super().__str__() + f", max print speed: {self.max_print_speed} pages per minute"

class Scanner(OfficeEquipment):
    def __init__(self, model, price, year, max_scan_resolution):
        super().__init__(model, price, year)
        self.max_scan_resolution = max_scan_resolution

    def __str__(self):
        return super().__str__() + f", max scan resolution: {self.max_scan_resolution} dpi"

class Xerox(OfficeEquipment):
    def __init__(self, model, price, year, max_copy_speed):
        super().__init__(model, price, year)
        self.max_copy_speed = max_copy_speed

    def __str__(self):
        return super().__str__() + f", max copy speed: {self.max_copy_speed} pages per minute"

class Warehouse:
    def __init__(self):
        self.equipment = {}

    def add_equipment(self, equipment, quantity):
        if not isinstance(quantity, int) or quantity < 1:
            raise ValueError("Invalid quantity")
        if equipment not in self.equipment:
            self.equipment[equipment] = quantity
        else:
            self.equipment[equipment] += quantity

    def remove_equipment(self, equipment, quantity):
        if not isinstance(quantity, int) or quantity < 1:
            raise ValueError("Invalid quantity")
        if equipment not in self.equipment or self.equipment[equipment] < quantity:
            raise ValueError("Not enough equipment")
        self.equipment[equipment] -= quantity

    def move_equipment(self, equipment, quantity, department):
        self.remove_equipment(equipment, quantity)
        department.receive_equipment(equipment, quantity)

class Department:
    def __init__(self, name):
        self.name = name
        self.equipment = {}

    def receive_equipment(self, equipment, quantity):
        if not isinstance(quantity, int) or quantity < 1:
            raise ValueError("Invalid quantity")
        if equipment not in self.equipment:
            self.equipment[equipment] = quantity
        else:
            self.equipment[equipment] += quantity
