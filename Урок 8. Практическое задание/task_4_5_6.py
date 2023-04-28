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


class ErrorPrice(Exception):
    pass


class Storage:
    my_storage = None


class OfficeEquipment(ABC):
    responsible_person = 'Bob'
    name = None
    max_price = None

    def __init__(self, color='white', model='Toshiba 7x', price=300):
        self.color = color
        self.model = model
        self.price = price

    def __str__(self):
        try:
            if self.price > self.max_price:
                raise ErrorPrice('Превышена максимальная цена товара. ')
        except ErrorPrice as ep:
            print(ep)
        else:
            print(f'{self.name} {self.model} успешно преобретен за ${self.price}')
            Storage.my_storage[{self.name}] += 1
        finally:
            return 'Bye!'


class Printer(OfficeEquipment):
    max_price = 300
    name = 'Принтер'


class Scanner(OfficeEquipment):
    max_price = 250
    name = 'Сканер'


class Xerox(OfficeEquipment):
    max_price = 480
    name = 'Ксерокс'


pr_by = Printer('Red', 'MXX', 13)
print(pr_by)
