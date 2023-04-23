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


class NumberCheck(Exception):
    def __init__(self, txt):
        self.txt = txt


class StrCheck(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeEquipmentWarehouse:
    def __init__(self, warehouse_space):
        self.warehouse_volume = warehouse_space
        if type(warehouse_space) != int and type(warehouse_space) != float:
            raise NumberCheck('Введите число')
        self.warehouse_items = []
        self.remaining_space = warehouse_space

    def add_equipment(self, equipment):
        self.warehouse_items.append(equipment)
        self.remaining_space -= equipment.items_volume
        if self.remaining_space < 0:
            self.warehouse_items.pop()
            self.remaining_space += equipment.items_volume
            print(f'Склад полон. Товар не принят. Осталось {self.remaining_space} места для хранения.')
        elif self.remaining_space < 0.1 * self.warehouse_volume:
            print(f'Место на складе заканчивается. {equipment} принят на склад.\n'
                  f'Осталось {self.remaining_space} места для хранения.\n')
        else:
            print(f'{equipment} принят на склад.\n'
                  f'Осталось {self.remaining_space} места для хранения.\n')

    def remove_equipment(self, destination, item_name, quantity):
        for el in self.warehouse_items:
            if item_name in el.values():
                el['Количество'] -= quantity
                if el['Количество'] == 0:
                    self.warehouse_items.remove(el)
                    print(f'{quantity} {el.discr().lower()}ов {item_name} переданы в подразделение {destination}')
                elif el['Количество'] < 0:
                    print('Недостаточно товара на складе.')
                    el['Количество'] += quantity
                elif el['Количество'] > 0:
                    self.remaining_space -= el['Количество'] * el['Объем одного устройства']
                    print(f'{quantity} {el.discr().lower()}ов {item_name} переданы в подразделение {destination}')
                else:
                    print('Error')
                break

    def inventory_check(self):
        print('\nИнвентаризация')
        equipment_volume = 0
        for el in self.warehouse_items:
            print(el)
            equipment_volume += el['Количество'] * el['Объем одного устройства']
        print(f'Объем техники {equipment_volume}\n')


class OfficeEquipment(ABC):
    def __init__(self, item_name, quantity, unit_volume):
        self.item_name = item_name
        if type(item_name) != str:
            raise StrCheck('Введите название устройства')
        self.quantity = quantity
        if type(quantity) != int:
            raise NumberCheck('Введите число')
        self.unit_volume = unit_volume
        if type(unit_volume) != int and type(unit_volume) != float:
            raise NumberCheck('Введите число')
        self.items_volume = unit_volume * quantity
        self.item_dict = {'Устройство': self.item_name,
                          'Количество': self.quantity,
                          'Объем одного устройства': self.unit_volume}

    def __str__(self):
        return str(self.item_dict)

    def __mul__(self, other):
        return self.unit_volume * self.quantity

    def values(self):
        return self.__dict__.values()

    def __setitem__(self, key, value):
        self.item_dict[key] = value

    def __getitem__(self, key):
        return self.item_dict[key]

    @abstractmethod
    def discr(self):
        return ' '


class Printer(OfficeEquipment):
    def action(self):
        return 'Печать'

    def discr(self):
        return 'Принтер'


class Scanner(OfficeEquipment):
    def action(self):
        return 'Скан'

    def discr(self):
        return 'Сканер'


class Duplicator(OfficeEquipment):
    def action(self):
        return 'Копия'

    def discr(self):
        return 'Копировальный аппарат'


office_warehouse = OfficeEquipmentWarehouse(500)
printer1 = Printer('Epson', 500, 0.03)
scanner1 = Scanner('HP', 1000, 0.01)
duplicator1 = Duplicator('Xerox', 800, 0.2)
office_warehouse.add_equipment(printer1)
office_warehouse.add_equipment(scanner1)
office_warehouse.inventory_check()
office_warehouse.add_equipment(duplicator1)
office_warehouse.inventory_check()
office_warehouse.remove_equipment('Отдел внедрения', 'Xerox', 100)
office_warehouse.inventory_check()
