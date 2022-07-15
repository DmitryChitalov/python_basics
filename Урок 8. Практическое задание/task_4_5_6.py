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


class Wirehouse:
    '''
    объект Склад:
        обладает атрибутом name
        содержит методы получения на склад
        выдачи со склада (в сторону другого склада)
        выдачи подробной информации по объектам, имеющимся на складе
    '''

    def __init__(self, name):
        self.my_wirehouse = []
        self.name = name

    def reception(self, unit: classmethod, count):
        for i in range(count):
            self.my_wirehouse.append(unit)

    def extradition(self, unit: classmethod, count):
        i = 0
        n = 0
        for i in range(len(self.my_wirehouse)):
            if self.my_wirehouse[i] == unit and n < count:
                self.my_wirehouse.remove(unit)
                n += 1
                if n == count:
                    break
                i = 0
            i += 1

    def get_detail(self):
        for el in self.my_wirehouse:
            print(el)

    def __str__(self):
        return f'Количество товаров на складе {self.name} {len(self.my_wirehouse)}'


class OfficeEquipment:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer


class Printer(OfficeEquipment):
    def __init__(self, manufacturer, is_colored: bool):
        super().__init__(manufacturer)
        self.is_colored = is_colored

    def __str__(self):
        return f'Принтер марки {self.manufacturer}. Возможность цветной печати: {self.is_colored}'


class Scaner(OfficeEquipment):
    body = {1: "portable", 2: "standalone"}

    def __init__(self, manufacturer, body_type):
        super().__init__(manufacturer)
        self.body = Scaner.body.get(body_type)

    def __str__(self):
        return f'Сканер марки {self.manufacturer}. Исполнение: {self.body}'


class Copier(OfficeEquipment):
    def __init__(self, manufacturer, bilateral: bool):
        super().__init__(manufacturer)
        self.bilateral = bilateral

    def __str__(self):
        return f'Копир марки {self.manufacturer}. Двустороннее копирование: {self.bilateral}'


class ExitCode(Exception):
    def __init__(self, txt):
        self.txt = txt


def transfer(from_wirehouse: Wirehouse, to_wirehouse: Wirehouse, unit: [Printer, Copier, Scaner], count):
    '''

    :param from_Wirehouse: с какого склада
    :param to_Wirehouse: на какой склад
    :param unit: какое устройство
    :param count: количество
    :return: Возвращает ExitCode операции. 0 - все ок, 1 - недостаточное количество на складе
    '''
    try:
        if from_wirehouse.my_wirehouse.count(unit) >= count:
            from_wirehouse.extradition(unit, count)
            to_wirehouse.reception(unit, count)
            raise ExitCode('0')
        else:
            raise ExitCode('1')
    except ExitCode as err:
        return err


printer = Printer('Epson', True)
scaner = Scaner('HP', 1)
copier = Copier('Xerox', False)

local_wirehouse = Wirehouse('Основной Склад')
office_wirehouse = Wirehouse('Офис')
print(local_wirehouse)
local_wirehouse.reception(printer, 10)
local_wirehouse.reception(scaner, 5)
local_wirehouse.reception(copier, 3)
local_wirehouse.reception(printer, 6)

print(local_wirehouse)
print(transfer(local_wirehouse, office_wirehouse, printer, 3))
print(local_wirehouse)
print(office_wirehouse)
local_wirehouse.get_detail()

print(transfer(office_wirehouse, local_wirehouse, scaner, 10))
