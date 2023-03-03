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

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_warehouse_full = []
        self.my_warehouse = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед. товара': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Ввод модели устройства: ')
            price = int(input(f'Ввод цены за единицу в рублях: '))
            qty = int(input(f'Ввод количества товара: '))
            unique = {'Модель устройства': unit, 'Цена за ед.товара': price, 'Количество': qty}
            self.my_unit.update(unique)
            self.my_warehouse.append(self.my_unit)
            print(f'Текущий список: \n {self.my_warehouse}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода ввести n, для продолжения нажать Enter (ввод)')
        q = input()
        if q == 'n':
            self.my_warehouse_full.append(self.my_warehouse)
            print(f'Весь склад: \n {self.my_warehouse_full}')
            return f'Выход '
        else:
            return Warehouse.reception(self)


class Printer(Warehouse):
    def to_print(self):
        return f'напечатать стр.{self.numb} раз'


class Scanner(Warehouse):
    def to_scan(self):
        return f'отсканировать лист {self.numb} раз'


class Copier(Warehouse):
    def to_copier(self):
        return f'копировать лист {self.numb} раз'


unit_1 = Printer('Samsung', 8500, 10, 30)
unit_2 = Scanner('HP', 6550, 7, 25)
unit_3 = Copier('Xerox', 4600, 3, 33)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_2.to_scan())
print(unit_3.to_copier())
