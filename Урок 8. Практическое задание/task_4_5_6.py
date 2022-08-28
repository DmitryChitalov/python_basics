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
from abc import ABC

class WareHouse:
    '''Склад'''
    storage = {}
    journal = []
    def add(self, item):
        '''Приемка на склад'''
        try:
            target = self.storage[item.__class__.__name__][item.inv_number]
            target.append(item)
        except KeyError:
            items_list = [item]
            try:
                self.storage[item.__class__.__name__][item.inv_number]  = items_list
            except KeyError:
                self.storage[item.__class__.__name__] = {item.inv_number: items_list}
        return f'Добавлено: {item.__dict__}'
    def give_by_item(self, item, division):
        '''Отдача по определенному объекту'''
        try:
            target = self.storage[item.__class__.__name__][item.inv_number]
            if item in target:
                target.remove(item)
                self.journal.append((len(self.journal) + 1, item,
                f'с классом: {item.__class__.__name__}',
                f'было выдано: {division}'))
                return item, f' выдано: {division}'
            else:
                return 'Объекта уже нет на складе'
        except KeyError:
            return 'Объекта с данным классом и артикулом нет на складе'
    def give_by_class(self, cls, division):
        '''Отдать по классу'''
        try:
            target_classes = self.storage[cls.__name__]
            for k, v in target_classes.items():
                if len(v) > 0:
                    target = v
                    item = v[0]
                    target.remove(item)
                    self.journal.append((len(self.journal) + 1, item,
                    f'с классом: {item.__class__.__name__}',
                    f'было выдано: {division}'))
                    return item, f' выдано: {division}'
                else:
                    return 'Объекта уже нет на складе'
        except KeyError:
            return 'Объекта с данным никогда не было на складе'

class StringDescr:
    '''Дескриптор для валидации на строку'''
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.my_attr} должно быть строкой')
        instance.__dict__[self.my_attr] = value
    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

class IntDescr:
    '''Дескриптор для валидации на число'''
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'{self.my_attr} должно быть числом')
        instance.__dict__[self.my_attr] = value
    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

class OfficeEquipment(ABC):
    '''оргтехника'''
    brand = StringDescr()
    model = StringDescr()
    inv_number = IntDescr()
    def __init__(self, brand, model,
    inv_number):
        self.brand = brand
        self.model = model
        self.inv_number = inv_number #артикул
    def __str__(self):
        return str(self.__dict__)


class Printer(OfficeEquipment):
    '''принтер'''
    dev_type = StringDescr()
    print_type = StringDescr()
    print_speed = IntDescr()
    def __init__(self, brand, model,
    inv_number, dev_type, print_type, print_speed):
        self.dev_type = dev_type #струйный/лазерный
        self.print_type = print_type # цвет/чб
        self.print_speed = print_speed #страниц в минуту
        super().__init__(brand, model, inv_number)


class Scanner(OfficeEquipment):
    '''сканер'''
    scan_type = StringDescr()
    max_letter_type = StringDescr()
    max_dpi = IntDescr()
    def __init__(self, brand, model, inv_number,
    scan_type, max_letter_type, max_dpi):
        self.scan_type = scan_type #лоток/планшет
        self.max_letter_type = max_letter_type #Формат бумаги
        self.max_dpi = max_dpi #макс разрешение
        super().__init__(brand, model, inv_number)

class Xerox(Printer, Scanner):
    '''ксерокс'''
    def __init__(self, brand, model, inv_number, dev_type, print_type,
    print_speed,scan_type, max_letter_type, max_dpi):
        self.brand = brand
        self.model = model
        self.inv_number = inv_number
        self.dev_type = dev_type
        self.print_type = print_type
        self.print_speed = print_speed
        self.scan_type = scan_type
        self.max_letter_type = max_letter_type
        self.max_dpi = max_dpi

wh = WareHouse()
xer_1 = Xerox('brand','model', 12,'dev_type',
'print_type', 48, 'scan_type', 'max_letter_type', 620)
xer_2 = Xerox('brand','model', 12344,'dev_type',
'print_type', 48, 'scan_type', 'max_letter_type', 320)
xer_3 = Xerox('brand','model', 50,'dev_type',
'print_type', 48, 'scan_type', 'max_letter_type', 320)
printer_1 = Printer('brand', 'model', 134, 'dev_type', 'print_type', 12)
printer_2 = Printer('brand', 'model', 135, 'dev_type', 'print_type', 12)
scanner_1 = Scanner('brand', 'model', 332, 'scan_type', 'max_letter_type', 620)

print('Добавляем на склад')
wh.add(xer_1)
wh.add(xer_2)
wh.add(xer_3)
wh.add(printer_1)
wh.add(scanner_1)
wh.add(printer_2)
print('Итого на складе:')
print(wh.storage)

print()

print('Отдаем со скалада по предметам')
wh.give_by_item(xer_2, 'бухгалтерия')
wh.give_by_item(xer_1, 'IT')

print('Пробуем отдать то, что было отдано:')
print(wh.give_by_item(xer_1, 'Директор'))

print()

print('Отдаем по типам устройства:')
wh.give_by_class(Printer,'Юр. деп')
wh.give_by_class(Scanner,'Юр. деп')
print()

print("Проверяем, что осталось:")
print(wh.storage)

print("Проверяем, журнал выдачи:")
print(wh.journal)
