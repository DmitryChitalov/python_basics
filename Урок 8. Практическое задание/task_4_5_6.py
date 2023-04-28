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
class Stock:
    spread = {}
    def __init__(self, row, shelf):
        self.row = row
        self.shelf = shelf
    def unpack_things(self, name_prod):
        a = 0
        for key in self.spread:
            print(key, end=' ')
            if key == name_prod:
                a = self.spread[key]
                a += 1
        if a == 0:
            self.spread[name_prod] = 1
        name_prod.print_name()
        print(f"в количестве {self.spread[name_prod]}")
    def giv_away(self, name_prod):
        a = 0
        for key in self.spread:
            print(key, end=' ')
            if key == name_prod:
                a = self.spread[key]
                if a > 1:
                    a -= 1
                    self.spread[key] = a
                elif a == 1:
                    self.spread.pop(key, None)
                    print("Продукт закончился")
        if a == 0:
            print("Нет такого продукта или закончился")
        if a == 0:
            print("Нет такого продукта")

class  Office_equipment:
    def __init__(self, name):
        self.name = name

class Printer(Office_equipment):
    def __init__(self, name, model):
        super().__init__(name)
        self. model = model
    def print_name(self):
        print(f"товар {self.name}_{self.model}", end= " ")

class Scanner(Office_equipment):
    def __init__(self, name, model):
        super().__init__(name)
        self. model = model

class Xerox(Office_equipment):
    def __init__(self, name, model):
        super().__init__(name)
        self. model = model

my_stock = Stock(3,3)
canon_r5 = Printer ("canon", "r5")
xerox_b2 = Xerox("xerox", "b2")
hp_a1 = Scanner("hp", "a1")

my_stock.unpack_things(canon_r5)

a2 = input("Введите список принтеров для отправки : ")
try:
    a2 = int(a2)
except ValueError:
  print("Вы ввели не число")
