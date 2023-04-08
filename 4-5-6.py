"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад
и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""


class MyError(Exception):
    def __init__(self, text):
        self.txt = text


class OfficeEquipment:

    def __init__(self, eq_type, name, price, quantity):
        self.type = eq_type
        self.name = name
        self.price = price
        try:
            if isinstance(quantity, int):
                self.quantity = quantity
                self.my_unit = {
                    'Тип устройства': self.type,
                    'Модель устройства': self.name,
                    'Цена за ед': self.price,
                    'Количество': self.quantity}
            else:
                self.my_unit = {}
                raise MyError("Ошибка ввода данных")
        except MyError as exc:
            print(exc)

    def __str__(self):
        return f'{self.type} {self.name} {self.price} {self.quantity}'


class Storage:
    goods = []

    @classmethod
    def reception(cls, obj):
        cls.goods.append(obj.my_unit)

    @classmethod
    def put_to_div(cls, obj, div):
        pass


class Printer(OfficeEquipment):
    def __init__(self, speed, eq_type, name, price, quantity):
        super().__init__(eq_type, name, price, quantity)
        self.speed = speed


class Scanner(OfficeEquipment):
    def __init__(self, colour, eq_type, name, price, quantity):
        super().__init__(eq_type, name, price, quantity)
        self.colour = colour


class Copier(OfficeEquipment):
    def __init__(self, copies, eq_type, name, price, quantity):
        super().__init__(eq_type, name, price, quantity)
        self.copies = copies


item_1 = Printer(354, 'Принтер', 'A1-230', 15000, 150)
item_2 = Scanner('белый', 'Сканер', 'Perle 2000', 20000, 28)
item_3 = Copier(1200, 'Ксерокс', 'Xerox GT2023', 42500, 107)

Storage.reception(item_1)
Storage.reception(item_2)
Storage.reception(item_3)

print(Storage.goods)
