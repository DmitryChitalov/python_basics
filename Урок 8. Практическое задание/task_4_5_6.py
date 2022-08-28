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
from collections import Counter


class Stock:
    _storage = []

    def coming(self, product):
        self._storage.append(product)

    @staticmethod
    def report():
        new_list = Counter(type(x).__name__ for x in Stock._storage)
        print(f"На складе всего продукции: {len(Stock._storage)} шт. из них по типам: ")
        for k, v in new_list.items():
            print(f"{k}: {v} шт.")

    @staticmethod
    def send(product_code, company_name):
        product_index = None
        for i in range(0, len(Stock._storage)):
            if Stock._storage[i].code == product_code:
                product_index = i
                break

        if product_index:
            print(f"Товар с кодом {product_code} не найден!")

        Stock._storage.pop(product_index)
        print(f"Товар с кодом {product_index} отправлен в компанию {company_name}")


class OfficeEquipment:
    def __init__(self, code, model):
        self.code = code
        self.model = model


class Xerography(OfficeEquipment):
    print_type = None
    is_color = None
    dpi = None

    def __init__(self, code, model, print_type, is_color, dpi):
        super(Xerography, self).__init__(code, model)
        self.code = code
        self.print_type = print_type
        self.is_color = is_color
        self.dpi = dpi
        self.model = model


class Printer(OfficeEquipment):
    print_type = None
    is_color = None

    def __init__(self, code, model, print_type, is_color):
        super(Printer, self).__init__(code, model)
        self.code = code
        self.print_type = print_type
        self.is_color = is_color
        self.model = model


class Scanner(OfficeEquipment):
    scan_speed = None
    dpi = None

    def __init__(self, code, model, scan_speed, dpi):
        super(Scanner, self).__init__(code, model)
        self.code = code
        self.scan_speed = scan_speed
        self.dpi = dpi
        self.model = model


product1 = Xerography(1, "Xerox", "Laser", False, 720)
product2 = Xerography(2, "Samsung", "Laser", True, 1080)

product3 = Printer(3, "HP", "Laser", False)
product4 = Printer(4, "Canon", "Inkjet", False)

product5 = Scanner(5, "Canon", 8, 720)
product6 = Scanner(6, "HP", 10, 600)
product7 = Scanner(7, "HP", 15, 800)

stock = Stock()
stock.coming(product1)
stock.coming(product2)
stock.coming(product3)
stock.coming(product4)
stock.coming(product5)
stock.coming(product6)
stock.coming(product7)

stock.report()
stock.send(7, 2)
stock.report()