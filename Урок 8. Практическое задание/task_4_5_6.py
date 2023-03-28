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

from typing import Dict

class OrgTechnic:
    def __init__(self, name: str):
        self.name: str = name

class Printer(OrgTechnic):
    def __init__(self, colored: bool):
        super().__init__('Printer')
        self.colored: bool = colored

class Scanner(OrgTechnic):
    def __init__(self, fmt: str):
        super().__init__('Scanner')
        self.fmt: str = fmt

class Xerox(OrgTechnic):
    def __init__(self, speed: int):
        super().__init__('Xerox')
        self.speed: int = speed

class Warehouse:
    def __init__(self):
        self.stock: Dict[str, int] = {}

    def get_quantity(self, technic: OrgTechnic) -> int:
        return self.stock.get(technic.name, 0)

    def allocate(self, technic: OrgTechnic, quantity: int) -> int:
        stockQuantity: int = self.get_quantity(technic) + quantity
        self.stock[technic.name] = stockQuantity
        return stockQuantity

    def relocate(self, technic, quantity: int) -> int:
        stock_quantity: int = self.get_quantity(technic)
        relocated: int = min(stock_quantity, quantity)
        self.stock[technic.name] = stock_quantity - relocated
        return relocated
    
    def print_info(self):
        for technic in self.stock:
            print(f'{technic}: {self.stock[technic]}')
        print()
    
class NotIntegerError(Exception):
    def __init__(self, txt):
        self.txt = f'Ошибка, ожидается число, получено - {txt}'

    def __str__(self):
        return self.txt

def inputNumber(str: str) -> int:
    while True:
        try:
            res = input(str)    
            if not res.isdigit():
                raise NotIntegerError(res)
            
            return int(res)
        
        except NotIntegerError as error:
            print(f'--> {error}')

def chooseTechnic() -> OrgTechnic:
    while True:
        name = input('>> Выберите оргтехнику (printer / scanner / xerox): ')
        if name == 'printer':
            colored = input('>>> цветной (y/n): ')
            if colored == 'y':
                return Printer(True)
            return Printer(False)
        
        if name == 'scanner':
            fmt = input('>>> формат (A2 / A3 / A4): ')
            return Scanner(fmt)
        
        if name == 'xerox':
            speed = inputNumber('>>> скорость: ')
            return Xerox(speed)
        
        print('--> Повторите ввод')

warehouse = Warehouse()

print('Введите команды для работы со складом')
print(' add - принять на склад')
print(' remove - передать со склада')
print(' info - вывести информация об остатках')
print(' exit - завершить работу')
while True:
    cmd = input('> Введите команду: ')
    if cmd == 'exit':
        break

    if cmd == 'add':
        technic = chooseTechnic()
        print(f'{technic.name}: {warehouse.get_quantity(technic)}')
        quantity = inputNumber('>> Количество передачи на склад: ')
        total = warehouse.allocate(technic, quantity)
        print(f'{technic.name}: {total}')
        continue

    if cmd == 'remove':
        technic = chooseTechnic()
        print(f'{technic.name}: {warehouse.get_quantity(technic)}')        
        quantity = inputNumber('>> Количество передачи со склада: ')
        total = warehouse.relocate(technic, quantity)
        print(f'{technic.name}: {warehouse.get_quantity(technic)}')   
        continue

    if cmd == 'info':
        warehouse.print_info()
        continue

    print('--> неизвестная команда {cmd}, попробуйте еще раз')
    
