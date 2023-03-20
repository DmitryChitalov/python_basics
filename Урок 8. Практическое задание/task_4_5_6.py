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


# from abc import ABC, abstractmethod

class MyError(Exception):

    # Constructor or Initializer
    def __init__(self, value):
        self.value = value

    # __str__ is to print() the value
    def __str__(self):
        return repr(self.value)


class Storehouse:
    items = []

    def __init__(self, name):
        self.name = name

    @classmethod
    def push(cls, OfficeEq_, count_):
        try:
            if type(count_) is int:
                cls.items.append({"Model": OfficeEq_, "Quantity": count_})
            else:
                raise MyError("Число должно быть положительным целым!")
        except MyError as err:
            print(err)

    @classmethod
    def pull(cls, OfficeEq_, count_, dep_):
        try:
            if type(count_) is int:
                cls.items.append({"Model": OfficeEq_, "Quantity": -count_, "Department": dep_})
            else:
                raise MyError("Число должно быть положительным целым!")
        except MyError as err:
            print(err)


class OfficeEq:
    count = 0

    def __init__(self, brand, model, country_of_origin, serial_number, format_):
        self.brand = brand
        self.model = model
        self.country_of_origin = country_of_origin
        self.serial_number = serial_number
        self.format = format_
        OfficeEq.count += 1

    @property
    def lable(self):
        return f"{self.brand + self.model}"


class Printer(OfficeEq):
    def __init__(self, brand, model, country_of_origin, serial_number, format_, IsColor, Type_of_Print, IsLAN):
        super().__init__(brand, model, country_of_origin, serial_number, format_)
        self.IsColor = bool(IsColor)
        self.Type_of_Print = Type_of_Print
        self.IsLAN = bool(IsLAN)


class Scaner(OfficeEq):
    def __init__(self, brand, model, country_of_origin, serial_number, format_, Paper_Capture):
        super().__init__(brand, model, country_of_origin, serial_number, format_)
        self.Paper_Capture = bool(Paper_Capture)


class Xerox(OfficeEq):
    def __init__(self, brand, model, country_of_origin, serial_number, format_, Volume):
        super().__init__(brand, model, country_of_origin, serial_number, format_)
        self.Volume = Volume


StoreHouseCentral = Storehouse("Esentuki")
printer001 = Printer("hp", "laserjet h2030", "china", "a100df781", "A3", True, "Laser", False)
scaner001 = Scaner("canon", "lp200", "taiwan", "zxq9001jkk", "A4", True)
StoreHouseCentral.push(printer001.lable, 5)
StoreHouseCentral.push(scaner001.lable, 3.5)
StoreHouseCentral.pull(printer001.lable, 3, "west-office")
print(Storehouse.items)
