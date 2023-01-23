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
class Sklad:
    def __init__(self, name=None, price=None, quantity=None, prim=None, o_type=None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.prim = prim
        self.o_type = o_type
        self.my_store = []

    def __str__(self):
        return f'{self.my_store}'

    def income(self):
        try:
            name = input(f'Введите наименование: ')
            price = float(input(f'Введите цену за ед. в руб.: '))
            quantity = int(input(f'Введите количество: '))
            prim = input(f'Введите особенности техники: ')
            o_type = input(f'Введите тип техники:(s-сканер, p-принтер, x-ксерокс)')
            item = {'Модель': name, 'Цена за ед': price, 'Количество': quantity, 'Особенности': prim, 'тип': o_type}
            self.my_store.append(item)
        except ValueError:
            print('Недопустимое значение!')
            print(f'{Sklad.income(self)}')


class Printer(Sklad):
    def __init__(self, name, price, quantity, prim, o_type):
        super().__init__(name, price, quantity, prim, o_type)
        item = {'Модель': self.name, 'Цена за ед': self.price, 'Количество': self.quantity,
                'Особенности': self.prim, 'тип': self.o_type}
        self.my_store.append(item)


class Scaner(Sklad):
    def __init__(self, name, price, quantity, prim, o_type):
        super().__init__(name, price, quantity, prim, o_type)
        item = {'Модель': self.name, 'Цена за ед': self.price, 'Количество': self.quantity,
                'Особенности': self.prim, 'тип': self.o_type}
        self.my_store.append(item)


class Xerox(Sklad):
    def __init__(self, name, price, quantity, prim, o_type):
        super().__init__(name, price, quantity, prim, o_type)
        item = {'Модель': self.name, 'Цена за ед': self.price, 'Количество': self.quantity,
                'Особенности': self.prim, 'тип': self.o_type}
        self.my_store.append(item)


p_1 = Scaner('panasonic', 2500, 20, "A-3", 's')
p_2 = Printer('kyocera', 1955.55, 2, 'лазерный', 'p')
p_3 = Xerox('sony', 2550.5, 5, 'цветной', 'x')
p_4 = Sklad()

print(p_1)
print(p_2)
print(p_3)
p_4.income()
print(p_4.my_store)
