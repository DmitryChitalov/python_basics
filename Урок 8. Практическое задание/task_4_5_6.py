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
    equipment_dict = {}

    def transfer(self, equipment):
        if not isinstance(equipment, Equipment):
            raise Exception('Ошибка!')
        if self.equipment_dict.get(equipment) is not None:
            self.equipment_dict[equipment] += 1
        else:
            self.equipment_dict[equipment] = 1

    def final_dict(self):
        for name, item in self.equipment_dict.items():
            print(f'{name} : {item} шт')


class Equipment:
    def __init__(self, brand, model, price, type_of):
        self.brand = brand
        self.model = model
        self.price = price
        self.type_of = type_of

    def __str__(self):
        return f"{self.brand} {self.model}"


class Printer(Equipment):
    def __init__(self, brand: str, model: str, price: int, type_of: str):
        super().__init__('Printer', brand, model, price)
        self.type = type_of


class Scanner(Equipment):
    def __init__(self, brand: str, model: str, price: int, resolution: str):
        super().__init__('Scanner', brand, model, price)
        self.resolution = resolution


class Xerox(Equipment):
    def __init__(self, brand: str, model: str, price: int):
        super().__init__('Xerox', brand, model, price)


printer_1 = Printer('HP', 'LaserJet', 10000, 'Лазерный')
printer_2 = Printer('Canon', 'Photo', 20000, 'Фото')
scanner_1 = Scanner('HP', 'SC-01', 5000, '3200*2400')
scanner_2 = Scanner('Canon', 'SC-001', 4000, '1600*1200')
xerox_1 = Xerox('HP', 'X-01', 5000)
xerox_2 = Xerox('Canon', 'X-001', 6000)
xerox_3 = Xerox('Xerox', 'X-1', 9000)
stock = OfficeEquipment()
stock.transfer(printer_1)
stock.transfer(scanner_2)
stock.transfer(xerox_3)
stock.final_dict()
