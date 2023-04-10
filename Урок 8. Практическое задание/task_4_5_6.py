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


class Storage:
    def __init__(self, name):
        self.name = name
        self.storage_items = {}

    def add_item(self, some_item, my_quantity):
        if some_item in self.storage_items:
            self.storage_items[some_item] += my_quantity
        else:
            self.storage_items[some_item] = my_quantity

    def remove_item(self, some_item, my_quantity):
        if some_item in self.storage_items:
            if self.storage_items[some_item] >= my_quantity >= 0:
                self.storage_items[some_item] -= my_quantity
            else:
                raise ValueError('Количество не может быть меньше нуля')
        else:
            raise ValueError('Такого предмета не существует')
        for my_item in [printer, scanner, copier]:
            if str(my_item) == some_item:
                my_item.quantity -= my_quantity

    def move_item(self, some_item, my_quantity, department):
        if not isinstance(my_quantity, int):
            raise ValueError('Количество должно быть целым числом!')
        if my_quantity <= 0:
            raise ValueError('Количество должно быть больше нуля!')
        if some_item in self.storage_items and my_quantity <= self.storage_items[some_item]:
            self.storage_items[some_item] -= my_quantity
            department.receive_item(some_item, my_quantity)
            for my_item in [printer, scanner, copier]:
                if str(my_item) == some_item:
                    my_item.quantity -= my_quantity
                    department.receive_item(str(my_item), my_quantity)
        else:
            raise ValueError('На складе нет такого количества')
        return self.storage_items

    def get_items(self):
        items = {}
        for my_item, my_quantity in self.storage_items.items():
            items[my_item] = my_quantity
        return items


class OfficeItem:
    def __init__(self, name, model, price, my_quantity):
        self.name = name
        self.model = model
        self.price = price
        self.quantity = my_quantity

    def __str__(self):
        return f"'{self.name}' {self.model}, цена: {self.price}$, начальное количество: {self.quantity} шт."


class Printer(OfficeItem):
    def __init__(self, name, model, price, my_quantity, print_type):
        super().__init__(name, model, price, my_quantity)
        self.print_type = print_type

    def __str__(self):
        return f"'{self.name}' {self.model}, цена: {self.price}$, начальное количество: {self.quantity} шт., " \
               f"тип печати: {self.print_type}"


class Scanner(OfficeItem):
    def __init__(self, name, model, price, my_quantity, scanner_type):
        super().__init__(name, model, price, my_quantity)
        self.scanner_type = scanner_type

    def __str__(self):
        return f"'{self.name}' {self.model}, цена: {self.price}$, начальное количество: {self.quantity} шт.," \
               f" тип сканирования: {self.scanner_type}"


class Copier(OfficeItem):
    def __init__(self, name, model, price, my_quantity, copying_speed):
        super().__init__(name, model, price, my_quantity)
        self.copying_speed = copying_speed

    def __str__(self):
        return f"'{self.name}' {self.model}, цена: {self.price}$, начальное количество: {self.quantity} шт.," \
               f" скорость копирования: {self.copying_speed}"


class Department:
    def __init__(self, name):
        self.name = name
        self.department_items = {}

    def receive_item(self, some_item, my_quantity):
        if my_quantity > 0:
            if some_item not in self.department_items:
                self.department_items[some_item] = my_quantity
            else:
                self.department_items[some_item] += my_quantity
            if self.department_items[some_item] < 0:
                raise ValueError('Количество не может быть меньше нуля')
            return
        raise ValueError('Количество должно быть целым числом')

    def get_items(self):
        items = {}
        for my_item, my_quantity in self.department_items.items():
            items[my_item] = my_quantity
        return items


storage = Storage("Склад")
development_department = Department("Отдел разработки")
accounting_department = Department("Бухгалтерия")

printer = Printer("Принтер", "Epson L3211", 250, 10, "лазерный")
scanner = Scanner("Сканер", "HP LaserJet Pro", 300, 3, "потоковый")
copier = Copier("Копир", "Pantum M6700DW", 200, 5, "высокая")

storage.add_item(str(printer), 10)
storage.add_item(str(scanner), 3)
storage.add_item(str(copier), 5)

print("Техника на складе:")
for item, quantity in storage.get_items().items():
    print(f"{item}, Остаток: {quantity} шт.")
