# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
# «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

class OfficeStuff:
    def __init__(self, name):
        self.name = name

class Printer(OfficeStuff):
    def can_print(self):
        return f'может печатать'


class Scanner(OfficeStuff):
    def can_scan(self):
        return f'может сканировать'


class Copier(OfficeStuff):
    def can_copy(self):
        return f'может копировать'


printer_1 = Printer('epson')
print(printer_1.can_print())

