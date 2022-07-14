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
    def __init__(self, printers, scaners, copiers, IT, Buhg, Adm):
        self.stock = dict(printers=len(printers), scaners=len(scaners), copiers=len(copiers))
        self.printers = printers
        self.scaners = scaners
        self.copiers = copiers
        self.IT = IT
        self.Buhg = Buhg
        self.Adm = Adm

    def reception(self, frm, what):
        self.frm = frm
        self.what = what

    def transfer(self, to, type, what):
        if type == 'printers':
            self.printers.remove(what)
        if to == 'IT':
            self.IT.append(what)


class OfficeEquipment:
    def __init__(self, model=None, vendor=None):
        self.model = model
        self.vendor = vendor


class Printer(OfficeEquipment):
    def __init__(self, model, vendor, ip):
        super().__init__(model, vendor)
        self.ip = ip


class Scaner(OfficeEquipment):
    def __init__(self, model, vendor, resolution):
        super().__init__(model, vendor)
        self.resolution = resolution


class Copier(OfficeEquipment):
    def __init__(self, model, vendor, speed):
        super().__init__(model, vendor)
        self.speed = speed


office = OfficeEquipment()
printer1 = Printer('Laser Jet 400', 'HP', '10.100.15.61')
printer2 = Printer('SM-125', 'Samsung', '10.100.15.62')
printer3 = Printer('XMKDDYJ01HT', 'Xiaomi', '10.100.15.63')
scaner1 = Scaner('EN 60950-1', 'Epson', '12800 dpi')
copier1 = Copier('3040', 'Xerox', '4,56 м/мин')
copier2 = Copier('EL-8434', 'Canon', '2,31 м/мин')

warehouse = Warehouse([printer1, printer2, printer3], [scaner1],
         [copier1, copier2], [], [], [])

print(warehouse.scaners[0].model)

warehouse.transfer('IT', 'printers', printer1)
print(warehouse.stock)

'''
Сделал не до конца но суть понятна.
'''