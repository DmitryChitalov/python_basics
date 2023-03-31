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
class Office(Exception):
    def __init__(self, text):
        self.text = text
class Office_equipment:
    def __init__(self, name, type, model, total):
        self.name = name
        self.type = type
        self.model = model
        try:
            if isinstance(total, int):
                self.total = total
                self.res = {'Модель': self.name, 'Тип': self.type, 'Кол-во': self.total}
            else:
                self.res = {}
                raise Office('Что-то не так')
        except Office as f:
            print(f.text)
class Stock:
    my_stock = []
    def __init__(self):
        self.stock_for_technique = []
    @classmethod
    def reception(cls, prod):
        cls.my_stock.append(prod.res)
    @classmethod
    def put_to_stock(cls, prod, div):
        pass

class Printer(Office_equipment):
    def __int__(self, name, type, model, total, color):
        super().__init__(name, type, model, total)
        self.color = color
    def __str__(self):
        return f'Printer ( name: {self.name}, type: {self.type}, model: {self.total}, total: {self.total}, color: {self.color})'
class Scaner(Office_equipment):
    def __int__(self, name, type, model, total, height):
        super().__init__(name, type, model, total)
        self.height = height

    def __str__(self):
        return f'Printer ( name: {self.name}, type: {self.type}, model: {self.total}, total: {self.total}, height: {self.height})'

class Xerox(Office_equipment):
    def __int__(self, name, type, model, total, style):
        super().__init__(name, type, model, total)
        self.style = style

    def __str__(self):
        return f'Printer ( name: {self.name}, type: {self.type}, model: {self.total}, total: {self.total},  height: {self.style})'

my_prin = Printer('LG','laser', 54, 'black')
my_scan = Scaner('LG', 'tnt', 43, 72)
my_cop = Xerox('LG', 'mtm', 2, 15)

Stock.reception(my_prin)
Stock.reception(my_scan)
Stock.reception(my_cop)

print(Stock.my_stock)
