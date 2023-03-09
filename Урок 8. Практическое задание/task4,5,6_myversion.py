"""
4:
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для
каждого типа оргтехники.
5:
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.
6:
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
уроках по ООП.
"""


class Warehouse:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.storage_full = []
        self.store = []
        self.product = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def my_store(self):
        try:
            name = input(f'Введите наименование ')
            price = int(input(f'Введите цену за ед '))
            quantity = int(input(f'Введите количество '))
            unique = {'Модель устройства': name, 'Цена за ед': price, 'Количество': quantity}
            self.product.update(unique)
            self.store.append(self.product)
            print(self.store)
        except ValueError:
            return f'Ошибка ввода данных'

        resume = input(f'Хотите продолжить? y/n: ')
        if resume == 'n':
            self.storage_full.append(self.store)
            print(f'Весь склад:\n {self.storage_full}')
        else:
            return Warehouse.my_store


class Printer(Warehouse):
    pass


class Scanner(Warehouse):
    pass


class Copier(Warehouse):
    pass


pro_1 = Printer('hp', 2000, 5)
pro_2 = Scanner('Canon', 1200, 5)
pro_3 = Copier('Xerox', 1500, 1)
pro_1.my_store()
pro_2.my_store()
pro_3.my_store()
