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
class Warehouse:
    def __init__(self):
        self.inventory = {} #хранения инвентаря

    def receiveitem(self, item, quantity):
        if not isinstance(quantity, int) or quantity <= 0: # проверка корректности количества
            raise ValueError("Неправильное количество")
        if item in self.inventory:
            self.inventory[item] += quantity # добавление количества к уже имеющемуся инвентарю
        else:
            self.inventory[item] = quantity # добавление нового инвентаря

    def transferitem(self, item, quantity, department):
        if not isinstance(quantity, int) or quantity <= 0: # проверка корректности количества
            raise ValueError("Неправильное количество")
        if item not in self.inventory or self.inventory[item] < quantity:# проверка наличия достаточного количества инвентаря
            raise ValueError("Мало инвентаря")
        self.inventory[item] -= quantity #уменьшение количества инвентаря на складе
        if item in department.inventory:
            department.inventory[item] += quantity# добавление количества инвентаря в отдел
        else:
            department.inventory[item] = quantity


class OfficeEquipment:# бренд, модель, цена
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, brand, model, price, color=False):
        super().__init__(brand, model, price)
        self.color = color  # цветной принтер или нет


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, price, resolution):
        super().__init__(brand, model, price)
        self.resolution = resolution # разрешение сканера


class Copier(OfficeEquipment):
    def __init__(self, brand, model, price, speed):
        super().__init__(brand, model, price)
        self.speed = speed# скорость копирования

class Department:
    def __init__(self):
        self.inventory = {}# словарь для хранения инвентаря в отделе

warehouse = Warehouse()
department1 = Department()
printer1 = Printer("HP", "LaserJet", 150)
scanner1 = Scanner("Epson", "Perfection", 100, "1200x2400 dpi")
copier1 = Copier("Canon", "ImageRunner", 200, "50 pages per minute")

try:
    warehouse.receiveitem(printer1, "two")# ошибка в количестве
except ValueError as e:
    print(e)

try:
    warehouse.transferitem(printer1, 1, department1)
except ValueError as e:# если Неправильное количество
    print(e)
