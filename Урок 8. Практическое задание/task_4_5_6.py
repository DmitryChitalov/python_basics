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
        self.dict = {}

    def add_to(self, equipment):
        ''' добавляем в словарь обьект по его названию, в значении
        будет список экземпляров этого оборудования'''
        self.dict.setdefault(equipment.group_name(), []).append(equipment)

    def send_to_management(self, name):
        ''' извлекаем из значения обьект по названию группы'''
        if self.dict[name]:
            self.dict.setdefault(name).pop(0)


class ControlType(Exception):
    pass


class Equipment:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.group = self.__class__.__name__
        # try:
        #     self.quantity = quantity
        #     if self.quantity == str(quantity):
        #         raise ControlType(self.quantity)
        # except ControlType as ex:
        #     print(f'{ex} - не число!')

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'Наименование: {self.name}. Количество: {self.quantity}шт. Цена за 1 шт: {self.price}'


class Printer(Equipment):
    def __init__(self, name, quantity, price, photo_printing=True):
        super().__init__(name, quantity, price)
        self.photo_printing = photo_printing


class Scanner(Equipment):
    def __init__(self, name, quantity, price, color_printing=False):
        super().__init__(name, quantity, price)
        self.color_printing = color_printing


class Xerox(Equipment):
    def __init__(self, name, quantity, price, guarantee):
        super().__init__(name, quantity, price)
        self.guarantee = {'guarantee period': guarantee}


'''Создаем объекты и добавляем на склад'''
printer = Printer('HP', 3, 6000, True)
scanner = Scanner('Canon', 2, 6500, True)
xerox = Xerox('Pantum', 2, 40000, 5)

w = Warehouse()
w.add_to(printer)
w.add_to(scanner)
w.add_to(xerox)

'''Выводим склад'''
print(w.dict)

'''Выводим объект со склада'''
w.send_to_management('Xerox')

'''Выводим склад'''
print(w.dict)
