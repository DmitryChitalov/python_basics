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

class Storage:
    def __init__(self, name):
        self.name = name
        self.inventory = {}

    def receive(self, item, quantity):
        if type(quantity) != int:
            print("Ошибка: количество должно быть целым числом")
            return
        if item.name not in self.inventory:
            self.inventory[item.name] = quantity
        else:
            self.inventory[item.name] += quantity

    def transfer(self, item, quantity, department):
        if type(quantity) != int:
            print("Ошибка: количество должно быть целым числом")
            return
        if item.name not in self.inventory or self.inventory[item.name] < quantity:
            print("Ошибка: недостаточное количество на складе")
            return
        if department not in item.departments:
            print("Ошибка: указанный отдел недействителен для данного товара")
            return
        if department not in self.inventory:
            self.inventory[department] = {}
        if item.name not in self.inventory[department]:
            self.inventory[department][item.name] = quantity
        else:
            self.inventory[department][item.name] += quantity
        self.inventory[item.name] -= quantity


class OfficeEquipment:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)


class Printer(OfficeEquipment):
    def __init__(self, name, price, weight, color, paper_size):
        super().__init__(name, price, weight)
        self.color = color
        self.paper_size = paper_size


class Scanner(OfficeEquipment):
    def __init__(self, name, price, weight, resolution):
        super().__init__(name, price, weight)
        self.resolution = resolution


class Xerox(OfficeEquipment):
    def __init__(self, name, price, weight, speed):
        super().__init__(name, price, weight)
        self.speed = speed
