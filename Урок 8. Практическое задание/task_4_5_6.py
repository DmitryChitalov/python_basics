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

from datetime import datetime
from pygments.formatters import other


class Depot:
    def __init__(self, title):
        self.title = title
        self.lists = {}
        self.give_lists = {}

    def take_to_depot(self, equipment):
        t = datetime.now()

        self.lists.update({equipment.serial_number: [equipment.title, self, t]})
        print(
            f'На склад ' + self.title + ' получено оборудование:' + '' + equipment.title + ' ,серийный номер - ' + str(
                equipment.serial_number) + ', Дата:' + str(t.day) + '.' + str(t.month) + '.' + str(t.year))

    def give_to_depot(self, equipment, other):
        t = datetime.now()

        self.give_lists.update({equipment.serial_number: [equipment.title, other, t]})
        print('Передано оборудование:' + '' + equipment.title + ', серийный номер -' + str(
            equipment.serial_number) + ',Дата:' + str(t.day) + '.' + str(t.month) + '.' + str(t.year))
        other.take_to_depot(equipment)

    def list_equipments(self):
        print('На склад' + self.title + 'получено оборудования:')
        print(self.lists)
        print('Общее количество: ', len(self.lists))
        print('Со Склада' + self.title + 'выдано оборудование:')
        print(self.give_lists)
        print('Общее количество', len(self.give_lists))


class Office_equipment:
    def __init__(self, title, serial_number):
        self.title = title
        self.serial_number = serial_number

    def __str__(self):
        return str(self.title)


class Printer(Office_equipment):
    def __init__(self, title, serial_number, print_velocity):
        Office_equipment.__init__(self, title, serial_number)
        self.print_velocity = print_velocity

    def __str__(self):
        return 'Название модели:' + Office_equipment.__str__(self) + ',Параметры:' + str(self.print_velocity)


class Scanner(Office_equipment):
    def __init__(self, title, serial_number, resolution):
        Office_equipment.__init__(self, title, serial_number)
        self.resolution = resolution

    def __str__(self):
        return 'Название модели:' + Office_equipment.__str__(self) + ',Параметры:' + str(self.resolution)


class Copier(Office_equipment):
    def __init__(self, title, serial_number, addit):
        Office_equipment.__init__(self, title, serial_number)
        self.addit = addit

    def __str__(self):
        return 'Название модели:' + Office_equipment.__str__(self) + ',Параметры:' + str(self.addit)


store1 = Depot('Main Warehouse')
store2 = Depot('Small Warehouse')
a = Printer('HP', 'GWRE65T87JKJJ8', 'Laser Printer')
b = Scanner('Epson', 'JK5G60T87GBKJJ8', 'ColorPhoto Printer')
c = Copier('Brother', 'LLKJ996FBSIR55342J623', 'Laser CopyMachine')
d = Printer('HP', 'H67JJFY8408FSDKL3', 'Unknown Printer')

print(a)
print(b)
print(c)

store1.take_to_depot(a)
store1.take_to_depot(b)
store2.take_to_depot(c)
store1.take_to_depot(d)
store2.take_to_depot(b)

store1.give_to_depot(b, store2)
store2.give_to_depot(c, store1)
