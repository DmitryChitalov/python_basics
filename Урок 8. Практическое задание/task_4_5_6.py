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

class EquipmentNotFoundException(Exception):
    pass


class Store:
    equipments = {}

    @staticmethod
    def incoming(new_equipments):
        for eq in new_equipments:
            if Store.equipments.keys().__contains__(type(eq)):
                Store.equipments[type(eq)].append(eq)
            else:
                Store.equipments[type(eq)] = [eq]

    @classmethod
    def get_count(cls, eq_type):
        try:
            return len(cls.equipments[eq_type])
        except KeyError:
            return 0

    @classmethod
    def transfer(cls, eq, target):
        if cls.equipments.keys().__contains__(type(eq)) == False or cls.equipments[type(eq)].__contains__(eq) == False:
            raise EquipmentNotFoundException('Equipment is out from store')
        cls.equipments[type(eq)].remove(eq)
        print(f'Equipment {eq} transfer at {target}')


class Equipment:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return self.model


class Printer(Equipment):
    def __init__(self, model, print_type):
        super().__init__(model)
        self.print_type = print_type


class Scanner(Equipment):
    def __init__(self, model, scan_size):
        super().__init__(model)
        self.scan_size = scan_size


class Copier(Equipment):
    def __init__(self, model, copy_type):
        super().__init__(model)
        self.copy_type = copy_type

def scan_store():
    print('Equipments in store:')
    v = Store.equipments.values()
    for types in v:
        for eq in types:
            print(eq)
    print(f'Printers in store: {Store.get_count(Printer)}')
    print(f'Scanners in store: {Store.get_count(Scanner)}')
    print(f'Copiers in store: {Store.get_count(Copier)}')


p1 = Printer("Printer 1", "Laser")
s1 = Scanner("Scanner 1", "A3")
c1 = Copier("Copier 1", "Manual")
c2 = Copier("Copier 2", "Automatic")
p2 = Printer("Printer 2", "Matrix")

Store.incoming([p1, s1, c1])
Store.incoming([p2])

scan_store()

try:
    print('Transfer equipment')
    Store.transfer(s1, "Бухгалтерия")
except EquipmentNotFoundException as ex:
    print(f'Equipment not transfer, because:\n{ex}')

scan_store()
