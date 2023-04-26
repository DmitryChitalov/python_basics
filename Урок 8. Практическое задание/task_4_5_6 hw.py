__author__ = 'AndreiM'
__version__ = "1.0 25.04.2023"
print("\n task_4_5_6 \n -------- \n")


class Store:
    def __init__(self, name, price, qty, num_lst, *args):
        self.name = name
        self.price = price
        self.qty = qty
        self.num = num_lst
        self.store_full = []
        self.store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед.': self.price, 'Кол-во': self.qty}

    def __str__(self):
        return f'{self.name} цена {self.price} кол-во {self.qty}'

    def input(self):
        try:
            unit = input(f'Введите наименование     : ')
            unit_p = int(input(f'Введите цену за одну ед. : '))
            unit_q = int(input(f'Введите количество       : '))
            unique = {'Модель устройства': unit, 'Цена за ед.': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.store.append(self.my_unit)
            print(f'Текущий список -\n {self.store}')
        except ValueError:
            return f'Ошибка ввода данных'

        print(f'Для выхода - q, продолжение - Enter')
        q = input(f'>>> ')
        if q == 'Q' or q == 'q':
            self.store_full.append(self.store)
            print(f'Весь склад -\n {self.store_full}')
            return f'Выход'
        else:
            return Store.input(self)

class Printer(Store):
    def to_print(self):
        return f'Печать возможна {self.num} раз'

class Scanner(Store):
    def to_scan(self):
        return f'Сканнирование возможно {self.num} раз'

class Copier(Store):
    def to_copier(self):
        return f'Копирование возможно  {self.num} раз'

unit_1 = Printer('Dell or HP', 2000, 1, 10)
unit_2 = Scanner('Dell or Canon', 7000, 1, 20)
unit_3 = Copier('Dell or Xerox', 6000, 1, 100)
print(unit_1.input())
print(unit_2.input())
print(unit_3.input())
print(unit_1.to_print())
print(unit_2.to_scan())
print(unit_3.to_copier())


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