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
class Myexc(Exception):
    def __init__(self, text):
        self.txt = text


class OfficeEquipment:
    def __init__(self, name, price, quantity, color):
        self.name = name
        self.price = price
        self.color = color
        try:
            if isinstance(quantity, int):

                self.quantity = quantity

                self.my_unit = {
                    'Модель устройства': self.name,
                    'Цена за ед': self.price,
                    'Количество': self.quantity}
            else:
                self.my_unit = {}
                raise Myexc("Ошибка ввода данных")

        except Myexc as exc:
            print(exc.text)


class Warehouse:
    goods = []

    @classmethod
    def reception(cls, obj):
        cls.goods.append(obj.my_unit)

    @classmethod
    def put_to_div(cls, obj, div):
        pass


class Printer(OfficeEquipment):
    def to_print(self):
        return f'Цвет {self.color}'


class Scanner(OfficeEquipment):
    def to_scan(self):
        return f'Цвет: {self.color}'


class Copier(OfficeEquipment):
    def to_copier(self):
        return f'Цвет:  {self.color}'


item_1 = Printer('Принтер', 150, 1, 'белый')
item_2 = Scanner('Сканер', 200, 2, 'серый')
item_3 = Copier('Ксерокс', 250, 3, 'белый')

Warehouse.reception(item_1)
Warehouse.reception(item_2)
Warehouse.reception(item_3)

print(Warehouse.goods)

print(item_1.to_print())
