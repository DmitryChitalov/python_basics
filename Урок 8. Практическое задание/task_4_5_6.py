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


class EquipmentWarehouse:

    def __init__(self, model_name, cost, quantity, number_of_lists):
        self.model_name = model_name
        self.cost = cost
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.model_name, 'Цена за ед': self.cost, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.model_name} цена {self.cost} количество {self.quantity}'

    def reception(self):
        try:
            device = input(f'Введите наименование ')
            device_c = int(input(f'Введите цену за ед '))
            device_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': device, 'Цена за ед': device_c, 'Количество': device_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - q, продолжение - Enter')
        q = input()
        if q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return EquipmentWarehouse.reception(self)


class Scanner(EquipmentWarehouse):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Printer(EquipmentWarehouse):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Copier(EquipmentWarehouse):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


device_1 = Scanner('Samsung', 3500, 10, 30)
device_2 = Printer('Epson', 3000, 8, 15)
device_3 = Copier('Xerox', 2000, 4, 30)
print(device_1.reception())
print(device_2.reception())
print(device_3.reception())
print(device_1.to_scan())
print(device_3.to_copier())
