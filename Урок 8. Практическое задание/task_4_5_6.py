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

    def add_to_wh(self, equipment):
        self.dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract_name(self, name):
        if self.dict[name]:
            self.dict.setdefault(name).pop(0)


class ControlType(Exception):
    pass


class Equipment:
    def __init__(self, name, quantity, price, guarantee, serial_num):
        self.name = name
        self.price = price
        self.guarantee = guarantee
        self.serial_num = serial_num
        self.group = self.__class__.__name__
        try:
            self.quantity = quantity
            if self.quantity == str(quantity):
                raise ControlType(self.quantity)
        except ControlType as ex:
            print(f'{ex} - не число')

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'Наименование: {self.name}. Количество: {self.quantity}шт. Цена за 1 шт: {self.price}.' \
               f'Гарантия: {self.guarantee}. Серийный №: {self.serial_num}'

class Monitor(Equipment):
    def __init__(self, name, quantity, price, guarantee, serial_num, diagonal, type_matrix, screen_resolution):
        super().__init__(name, quantity, price, guarantee, serial_num)
        self.diagonal = diagonal
        self.type_matrix = type_matrix
        self.screen_resolution = screen_resolution

class Printer(Equipment):
    def __init__(self, name, quantity, price, guarantee, serial_num, format_printing, speed_printing, color_printing=False):
        super().__init__(name, quantity, price, guarantee, serial_num)
        self.format_printing = format_printing
        self.speed_printing = speed_printing
        self.photo_printing = color_printing


class Scanner(Equipment):
    def __init__(self, name, quantity, price, guarantee, serial_num, scan_speed, scan_resolution, duplex_auto=False):
        super().__init__(name, quantity, price, guarantee, serial_num)
        self.scan_speed = scan_speed
        self.scan_resolution = scan_resolution
        self.duplex_auto = duplex_auto


'''Создаем объекты и добавляем на склад'''
monitor = Monitor(input('Введите наименование: '),
                  int(input('Введите количество: ')),
                  input('Введите цену: '),
                  input('Введите срок гарантии: '),
                  input('Введите серийный №: '),
                  input('Введите диагональ экрана: '),
                  input('Введите тип матрицы: '),
                  input('Введите разрешение экрана: '))

printer = Printer(input('Введите наименование: '),
                  int(input('Введите количество: ')),
                  input('Введите цену: '),
                  input('Введите срок гарантии: '),
                  input('Введите серийный №: '),
                  input('Введите формат печати: '),
                  input('Введите скорость печати стр/мин: '),
                  bool(input('Цветная печать True/False: ')))

scanner = Scanner(input('Введите наименование: '),
                  int(input('Введите количество: ')),
                  input('Введите цену: '),
                  input('Введите срок гарантии: '),
                  input('Введите серийный №: '),
                  input('Введите скорость сканирования стр/мин: '),
                  input('Введите разрешение сканирования: '),
                  bool(input('Дуплекс True/False: ')))

wh = Warehouse()
wh.add_to_wh(monitor)
wh.add_to_wh(printer)
wh.add_to_wh(scanner)

print(wh.dict)
wh.extract_name('Printer')
print(wh.dict)
