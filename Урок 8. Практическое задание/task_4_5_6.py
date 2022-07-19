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
    _departments = ['ИТ', 'АХО', 'Продажи', 'Бухгалтерия']

    def __init__(self, max_count):
        self.items = []
        self.max_count = max_count
        self._transferred = {}

    def __validate(self, item):
        if not isinstance(item, OfficeEquipment):
            raise ValueError(f"Это не офисная техника: {type(item)}")
        elif len(self.items) >= self.max_count:
            raise ValueError('Склад переполнен!')

    def add_items(self, items):
        for item in items:
            self.__validate(item)
            self.items.append(item)
            print(f'Оборудование {item.name} принято на склад.'
                  f'Количество: {len(self.items)}')

    def add_item(self, item):
        self.__validate(item)
        self.items.append(item)
        print(f'Оборудование {item.name} принято на склад.'
              f'Количество: {len(self.items)}')

    def transfer_item_to_department(self, item, department):
        if item not in self.items:
            print('Такого оборудования нет на складе!')
            return
        if department not in self._transferred:
            self._transferred[department] = []
        self._transferred[department].append(item)
        print(f'Оборудование {item.name} перемещено в отдел '
              f'{self._departments[department]}.')
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
            unit = input('Введите наименование: ')
            unit_p = int(input('Введите стоимость: '))
            type = int(input('Выберите тип'
                             '(0 - принтер, 1 - сканер, 2 - МФУ): '))
        except ValueError as err:
            print(f'Некорректный ввод! f"Ошибка {err=}, {type(err)=}')
            return

        if type == 0:
            return Printer(unit, unit_p)
        if type == 1:
            return Scanner(unit, unit_p)
        if type == 2:
            return Copier(unit, unit_p)

    def __str__(self):
        return f'Наименование: {self.name}; стоимость: {self.price}'


class Printer(OfficeEquipment):
    def pass_to_output(self, number_of_lists):
        return f'для печати {number_of_lists} листов'


class Scanner(OfficeEquipment):
    def pass_to_output(self, number_of_lists):
        return f'для сканирования {number_of_lists} листов'


class Copier(OfficeEquipment):
    def pass_to_output(self, number_of_lists):
        return f'для копирования {number_of_lists} листов'


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
