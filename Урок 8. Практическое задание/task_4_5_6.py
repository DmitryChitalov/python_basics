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

6. Продолжить работу над пятым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeEquipment:

    def __init__(self, model, quantity):

        # категория
        self.category = ''

        if type(self).__name__ == "Printer":
            self.category = "Принтер"
        if type(self).__name__ == "Scanner":
            self.category = "Сканер"
        if type(self).__name__ == "Copier":
            self.category = "Ксерокс"
        # self.category = self.__class__.__name__

        self.model = model

        try:
            if type(quantity) is int:
                self.quantity = quantity
                self.product = {
                    'Категория': self.category,
                    'Модель': self.model,
                    'Количество': self.quantity}
            else:
                self.product = {}
                raise MyException("Необходимо указать целое число. Данные не будут записаны.")

        except MyException as e:
            print(e.txt)

    def __add__(self, other):
        if self.category == other.category and self.model == other.model:
            return OfficeEquipment(self.model, self.quantity + other.quantity)

    def __sub__(self, other):
        if self.category == other.category and self.model == other.model:
            return OfficeEquipment(self.model, self.quantity - other.quantity)

    def __str__(self):
        return f'Категория: {self.category}, ' \
               f'Модель: {self.model}, ' \
               f'Количество: {self.quantity}'


class Warehouse:
    products = []

    @classmethod
    def add_to(cls, obj):
        _is_not_find = True

        if len(cls.products) == 0:
            cls.products.append(obj.product)
        else:
            for el in cls.products:
                if (el['Категория'] + el['Модель']) == (obj.category + obj.model):
                    el['Количество'] += obj.quantity
                    _is_not_find = False
                    break
            if _is_not_find:
                cls.products.append(obj.product)

    @classmethod
    def put_to_location(cls, obj, loc):
        _is_not_find = True

        if len(cls.products) == 0:
            print("Склад пустой")
        else:
            for el in cls.products:
                if (el['Категория'] + el['Модель']) == (obj.category + obj.model):
                    if el['Количество'] >= obj.quantity:
                        el['Количество'] -= obj.quantity
                        obj.location = loc
                        _is_not_find = False
                        break
                    else:
                        print("На складе нет такого количества техники")
            if _is_not_find:
                print("На складе нет такой техники")

    @staticmethod
    def get_info_list():
        for el in Warehouse.products:
            print(el)


class Printer(OfficeEquipment):

    def to_print(self):
        return f'Печать'


class Scanner(OfficeEquipment):
    def to_scan(self):
        return f'Сканирование'


class Copier(OfficeEquipment):
    def to_copier(self):
        return f'Копирование'


try:
    printers_1 = Printer('HP', 5)
    printers_2 = Printer('Epson', 9)
    printers_3 = Printer('HP', 7)
    printers_4 = Printer('Epson', 10)

    scanners_1 = Scanner('Canon', 3)
    copiers_1 = Copier('Kyocera', 2)

    Warehouse.add_to(printers_1)
    Warehouse.add_to(printers_2)
    Warehouse.add_to(printers_3)
    Warehouse.add_to(printers_4)

    Warehouse.add_to(scanners_1)
    Warehouse.add_to(copiers_1)

    print('-----------------------')
    print("Содержимое склада после пополнения:")
    Warehouse.get_info_list()

    Warehouse.put_to_location(printers_1, 'Блок управления персоналом')

    print()
    print(f'Список переданной техники в {printers_1.location}:')
    print(printers_1)

    print()
    print("Содержимое склада после уменьшения:")
    Warehouse.get_info_list()

    # print(printers1.to_print())

except:
    pass
