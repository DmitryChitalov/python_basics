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
import re


class Stock:
    def __init__(self):
        self.equipments = {}
        self.subdivision = {}

    def add_equipment(self, equipment, cnt):
        p = re.compile("^printer|scaner|xerox$")
        if not p.search(equipment):
            raise Exception('Нет такого оборудования')

        if self.equipments.get(equipment) is not None:
            cnt += self.equipments[equipment]
        self.equipments.update({equipment: cnt})

    def transfer_equipment(self, subdivision, equipment, cnt):
        equipment = str(equipment)
        if self.equipments.get(equipment) is None:
            raise Exception('Нет такой переферии борудования')
        if self.equipments[equipment] < cnt:
            raise Exception(f'Недостаточное кол-во техники доступно {self.equipments[equipment]}')
        self.equipments[equipment] -= cnt
        if self.subdivision.get(subdivision) is None:
            self.subdivision.update({subdivision: {equipment: cnt}})
        else:
            self.subdivision[subdivision].update({equipment: cnt})


class OfficeEquipment(ABC):
    def __init__(self, weight, power, speed):
        self.weight = weight
        self.power = power
        self.speed = speed

    @abstractmethod
    def print_speed(self):
        pass


class Printer(OfficeEquipment):
    def print_speed(self):
        print(f'Скорость печати принтера {self.speed} листов в минуту!')

    def __str__(self):
        return 'printer'


class Scaner(OfficeEquipment):
    def print_speed(self):
        print(f'Скорость сканирования {self.speed} листов в минуту!')

    def __str__(self):
        return 'scaner'


class Xerox(OfficeEquipment):
    def print_speed(self):
        print(f'Печать копий ксерокса {self.speed} листов в минуту!')

    def __str__(self):
        return 'xerox'


printer = Printer(800, 20, 15)
scaner = Scaner(300, 20, 25)
xerox = Xerox(1600, 20, 30)

printer.print_speed()
scaner.print_speed()
xerox.print_speed()

stock = Stock()
try:
    while True:
        equipment = input('Введите оборудование: ')
        if not equipment:
            break
        cnt = int(input('Введите количество: '))

        stock.add_equipment(equipment, cnt)

except Exception as err:
    print(err)

print(stock.equipments)

try:
    stock.transfer_equipment('Бухгалтерия', xerox, 4)
    stock.transfer_equipment('Бухгалтерия', printer, 1)
    stock.transfer_equipment('Лаборатория', printer, 1)
    stock.transfer_equipment('Секретарь', xerox, 1)
except Exception as err:
    print(err)

print(stock.subdivision)
print(stock.equipments)
