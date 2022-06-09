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
from abc import ABC, abstractmethod


class Warehouse:
    __max_count: int
    _items: list
    _transferred: dict
    _departments = ['HR', 'Engineers', 'Admins', 'Accounting']

    def __init__(self, max_count):
        self.items = []
        self.max_count = max_count
        self._transferred = {}

    def __validate(self, item):
        if not isinstance(item, OfficeEquipment):
            raise ValueError(f"Item does not belong to OfficeEquipment! Current type: {type(item)}")
        elif len(self.items) >= self.max_count:
            raise ValueError('The warehouse is full!')

    def add_items(self, items):
        for item in items:
            self.__validate(item)
            self.items.append(item)
            print(f'Item {item.name} was added to warehouse. Count: {len(self.items)}')

    def add_item(self, item):
        self.__validate(item)
        self.items.append(item)
        print(f'Item {item.name} was added to warehouse. Count: {len(self.items)}')

    def transfer_item_to_department(self, item, department):
        if item not in self.items:
            print('Such item is not available in the warehouse!')
            return
        if department not in self._transferred:
            self._transferred[department] = []
        self._transferred[department].append(item)
        print(f'Item {item.name} was transferred to {self._departments[department]} department.')
        self.items.remove(item)


class OfficeEquipment(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def pass_to_output(self, number_of_lists):
        pass

    @staticmethod
    def create_equipment():
        try:
            unit = input(f'Enter the name: ')
            unit_p = int(input(f'Enter the price: '))
            type = int(input(f'Enter the type (0 - printer, 1 - scanner, 2 - copier): '))
        except BaseException as error:
            print(f'Invalid input! f"Unexpected {error=}, {type(error)=}')
            return

        if type == 0:
            return Printer(unit, unit_p)
        if type == 1:
            return Scanner(unit, unit_p)
        if type == 2:
            return Copier(unit, unit_p)

    def __str__(self):
        return f'Name: {self.name}; price: {self.price}'


class Printer(OfficeEquipment):
    def pass_to_output(self, number_of_lists):
        return f'to print smth {number_of_lists} times'


class Scanner(OfficeEquipment):
    def pass_to_output(self, number_of_lists):
        return f'to scan smth {number_of_lists} times'


class Copier(OfficeEquipment):
    def pass_to_output(self, number_of_lists):
        return f'to copier smth  {number_of_lists} times'


unit1 = Printer('hp', 2000)
unit2 = Scanner('Canon', 1200)
unit3 = Copier('Xerox', 1500)
warehouse = Warehouse(2)
try:
    warehouse.add_item(unit1)
    warehouse.add_item(unit2)
    warehouse.transfer_item_to_department(unit2, 0)
    warehouse.transfer_item_to_department(unit3, 1)
    warehouse.add_item(unit3)
except BaseException as error:
    print(f"Unexpected {error=}, {type(error)=}")

unit4 = OfficeEquipment.create_equipment()
warehouse.transfer_item_to_department(unit3, 2)
warehouse.add_item(unit4)
warehouse.transfer_item_to_department(unit4, 3)
