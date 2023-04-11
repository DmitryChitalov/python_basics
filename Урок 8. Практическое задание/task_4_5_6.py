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


class Store:
    example_dict = {}

    def get_app(self, equipment):
        if not isinstance(equipment, Equipment):
            raise Exception('Внимание!')
        if self.example_dict.get(equipment) is not None:
            self.example_dict[equipment] += 1
        else:
            self.example_dict[equipment] = 1

    def result_dict(self):
        for k, v in self.example_dict.items():
            print(f'{k} : {v} шт')


class Equipment:
    def __init__(self, type_tech: str, brand: str, model: str, cost: float):
        self.type_tech = type_tech
        self.brand = brand
        self.model = model
        self.cost = cost

    def __str__(self):
        return f"{self.brand} {self.model}"


class Printer(Equipment):
    def __init__(self, brand: str, model: str, cost: float, type_: str):
        super().__init__('Printer', brand, model, cost)
        self.type = type_


class Scanner(Equipment):
    def __init__(self, brand: str, model: str, cost: float, interface: str):
        super().__init__('Scanner', brand, model, cost)
        self.interface = interface


class Xerox(Equipment):
    def __init__(self, brand: str, model: str, cost: float, dpi: str):
        super().__init__('Xerox', brand, model, cost)
        self.dpi = dpi


printer_1 = Printer('HP', 'Solaris', 1500, 'Струйный')
printer_2 = Printer('DEXP', 'Getway', 2500, 'Лазерный')

scanner_1 = Scanner('Intel', '001rft', 3000, 'Книжный')
scanner_2 = Scanner('AMD', 'LP034', 3200, 'Обычный')

xerox_1 = Xerox('Haier', 'UYTY12333', 3400, '1200 x 1200')
xerox_2 = Xerox('Razer', '232OP', 10000, '1600 x 1600')

store = Store()

store.get_app(printer_1)
store.get_app(printer_2)
store.get_app(scanner_1)
store.get_app(scanner_2)
store.get_app(scanner_2)

store.result_dict()
