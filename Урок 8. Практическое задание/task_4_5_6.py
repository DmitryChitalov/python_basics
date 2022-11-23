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

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
        
class Warehouse:
    all_stuff = []
    def __init__(self, device, name, price, quantity):
        self.device = device
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = {'Модель': self.name, 'Цена': self.price, 'Количество': self.quantity}

class Equipment(Warehouse):
    def add_to_wh(self, device):
        try:
            name = input('Введите название модели: ')
            price = input('Введите цену: ')
            quantity = input('Введите количество: ')
            if not price.isnumeric() or not quantity.isnumeric():
                raise OwnError('Ошибка ввода! Цена и количество должны быть числами!')
            item = {'Тип': device, 'Модель': name, 'Цена': price, 'Количество': quantity}
            self.items.update(item)
            print(self.items)
            self.all_stuff.append(self.items)
        except OwnError as err:
            print(err)

class Printer(Equipment):
    pass
    
class Scanner(Equipment):
    pass

class Xerox(Equipment):
    pass

printer = Printer('Принтер', 'HP', 30000, 5)
scanner = Scanner('Сканер', 'Brother', 10000, 3)
xerox = Xerox('Ксерокс', 'Xerox', 70000, 1)

while True:
    add_item = input('Ввести данные для принтера - p, сканера - s, ксерокса - x, для выхода - q: ')

    if add_item in ('p', 'P'):
        printer.add_to_wh(device='Принтер')
    elif add_item in ('s', 'S'):
        scanner.add_to_wh(device='Сканер')
    elif add_item in ('x', 'X'):
        xerox.add_to_wh(device='Ксерокс')
    elif add_item in ('q', 'Q'):
        break
    else:
        print('Ошибка! Повторите ввод.')

print(Warehouse.all_stuff)
