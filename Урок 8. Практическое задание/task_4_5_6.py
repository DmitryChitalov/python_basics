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


class OfficeDevices:

    def __init__(self, brand, model, type, format, price, quantity, *args):
        self.brand = brand
        self.model = model
        self.type = type
        self.format = format
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Марка: {brand}, Модель: {model}, Тип: {type}, Формат: {format}, Стоимость.: {uprice}, Количество: {uquantity}'

    def transfer(self):

        try:
            ubrand = input(f'Введите марку:')
            umodel = input(f'Введите модель:')
            utype = input(f'Введите тип (Соlor/Black):')
            uformat = input(f'Введите формат бумаги (А4,А3):')
            uprice = int(input(f'Введите стоимость:'))
            uquantity = int(input(f'Введите количество:'))
            unique = {'Марка': ubrand, 'Модель': umodel, 'Тип': utype, 'Формат': uformat, 'Стоимость.': uprice,
                      'Количество': uquantity}
            self.my_unit.update(unique)
            self.my_storage.append(self.my_unit)
            print(f'Введенные данные:\n{self.my_storage}')
        except Exception as e:
            return f'Ошибка при вводе данных! {e}'

        q = input(f'Для выхода введите - Q, для продолжения нажмите - Enter: ')
        if q == 'Q' or q == 'q':
            self.my_storage_full.append(self.my_storage)
            print(f'Наличие на складе:\n {self.my_storage_full}')
            return f'Выход'
        else:
            return OfficeDevices.transfer(self)


class Printer(OfficeDevices):
    def __init__(self, cartridge, *args):
        self.cartridge = cartridge
        self.my_unit = {}
        self.my_storage = []
        self.my_storage_full = []

    def to_print(self):
        return f'Картридж {self.cartridge} '


class Scanner(OfficeDevices):
    def __init__(self, autoscanner, *args):
        self.autoscanner = autoscanner
        self.my_unit = {}
        self.my_storage = []
        self.my_storage_full = []

    def to_scan(self):
        return f'Автоподатчик {self.autoscanner} '


class Copier(OfficeDevices):
    def __init__(self, cartridge, autoscanner, *args):
        self.cartridge = cartridge
        self.autoscanner = autoscanner
        self.my_unit = {}
        self.my_storage = []
        self.my_storage_full = []

    def to_copier(self):
        return f'Картридж {self.cartridge}, Автоподатчик {self.autoscanner} '


device_1 = Printer('CE310BL-CE311-CE312-CE313', 'HP', 'LaserJet CP1025', 'Color', 'A4', 32000, 1)
device_2 = Scanner('No', 'Canon', 'L120', 'Color', 'A4', 7600, 5)
device_3 = Printer('C13T67', 'EPSON', 'L1800', 'Color', 'A3', 67600, 2)
device_4 = Copier('1110', 'Auto', 'Kyocera', '1135', 'Black', 'A4', 47100, 1)
print(device_1.to_print())
print(device_2.to_scan())
print(device_3.to_print())
print(device_4.to_copier())
print(device_1.transfer())
