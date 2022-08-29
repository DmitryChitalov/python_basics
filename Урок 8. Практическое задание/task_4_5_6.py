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

class OfficeEquipment:

    def __init__(self, name, price, quantity, department):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.department = department
        self.my_store = []
        self.my_store_all = []
        self.my_department = []

    def income(self):
        off = True
        while off:
            self.items = {'Модель устройства': self.name, 'Цена за ед': self.price,
                          'Количество': self.quantity}
            self.department_items = {'Наименование отдела': self.department, 'Модель устройства': self.name,
                                     'Цена за ед': self.price, 'Количество': self.quantity}
            try:
                name = input(f'Введите наименование: ')
                price = int(input(f'Введите цену за ед: '))
                quantity = int(input(f'Введите количество: '))
                item = {'Модель устройства': name, 'Цена за ед': price, 'Количество': quantity}
                self.items.update(item)
                self.my_store.append(self.items)
                print(self.my_store)
                print('Для продолжения ввода нажмите Enter,\n для выхода Q, \n для передачи техники в отдел введите B')
                q = input()
                if q == 'q' or q == 'Q':
                    self.my_store_all.append(self.my_store)
                    print(f'Весь склад -\n {self.my_store_all}')
                    off = False
                if q == 'B' or q == 'b':
                    while off:
                        name = input(f'Введите модель: ')
                        for index in self.my_store:
                            for key, value in index.items():
                                if key == 'Модель устройства' and value == name:
                                    print(index)
                                    department = input(f'Введите отдел: ')
                                    department_items = {'Наименование отдела': department,
                                                        'Модель устройства': name, 'Цена за ед': price, 'Количество': quantity}
                                    self.department_items.update(department_items)
                                    self.my_department.append(self.department_items)
                                    self.my_store.remove(index)
                                    print(f'На основном складе осталось \n:{self.my_store}')
                                    print(f'Оборудование перемещено в отдел {department} \n {self.my_department}')
                                    off = False
            except ValueError:
                print('Недопустимое значение!')


class Printer(OfficeEquipment):
    pass


class Scanner(OfficeEquipment):
    pass


class Xerox(OfficeEquipment):
    pass


p = Xerox('Phaser', 12, 1233, 'Главный склад')
s = Scanner('Samsung', 15, 1000, 'Главный склад')
p = Printer('Hp', 2, 300, 'Главный склад')
p.income()

