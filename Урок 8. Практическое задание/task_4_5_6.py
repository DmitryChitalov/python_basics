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
class MyOfficeDevices(Exception):
    def __init__(self, txt):
        self.txt = txt
class OfficeDevices:
    def __init__(self, name, price, amount, quantity_lists):
        self.name = name
        self.price = price
        self.list = quantity_lists
        try:
            if isinstance(amount, int):
                self.amount = amount
                self.res = {
                    'Название модели': self.name,
                    'Цена за единицу товара (руб)': self.price,
                    'Количество (шт)': self.amount}
            else:
                self.res = {}
                raise MyOfficeDevices("Ошибка! Введены некорректные данные")
        except MyOfficeDevices as e:
            print(e.txt)
class Stock:
    goods = []
    @classmethod
    def reception(cls, prod):
        cls.goods.append(prod.res)
    @classmethod
    def put_to_div(cls, prod, div):
        pass

class Printer(OfficeDevices):
# класс-наследников Принтер
    def to_print(self):
        return f'Скорость печати текста страниц в минуту: {self.list}'

class Scanner(OfficeDevices):
# класс-наследников Сканер
    def to_scan(self):
        return f'Скорость сканирования страниц в минуту: {self.list}'

class Copier(OfficeDevices):
# класс-наследников Ксерокс
    def to_copier(self):
        return f'Скорость копирования страниц в минуту: {self.list}'

prin = Printer('Epson', 4900, 5, 14)
scan = Scanner('Canon', 9700, 4, 7)
cop = Copier('LG', 10600, 2, 15)
Stock.reception(prin)
Stock.reception(scan)
Stock.reception(cop)
print(Stock.goods)
print(scan.to_scan())
print(prin.to_print())
print(cop.to_copier())
