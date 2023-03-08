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
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return f"{self.name}: {self.price} руб., {self.weight} кг"


class Printer(OfficeEquipment):
    def __init__(self, name, price, weight, print_technology):
        super().__init__(name, price, weight)
        self.print_technology = print_technology

    def __str__(self):
        return f"{super().__str__()}, технология печати: {self.print_technology}"


class Scanner(OfficeEquipment):
    def __init__(self, name, price, weight, scan_resolution):
        super().__init__(name, price, weight)
        self.scan_resolution = scan_resolution

    def __str__(self):
        return f"{super().__str__()}, разрешение сканирования: {self.scan_resolution}"


class Xerox(OfficeEquipment):
    def __init__(self, name, price, weight, copy_speed):
        super().__init__(name, price, weight)
        self.copy_speed = copy_speed

    def __str__(self):
        return f"{super().__str__()}, скорость копирования: {self.copy_speed} страниц/мин"


class Warehouse:
    def __init__(self):
        self.storage = {}

    def add_item(self, item, quantity):
        if isinstance(quantity, int) and quantity > 0:
            if item in self.storage:
                self.storage[item] += quantity
            else:
                self.storage[item] = quantity
        else:
            print("Количество должно быть целым числом больше 0")

    def remove_item(self, item, quantity):
        if item in self.storage:
            if isinstance(quantity, int) and quantity > 0:
                if quantity > self.storage[item]:
                    print("На складе недостаточно товара")
                else:
                    self.storage[item] -= quantity
            else:
                print("Количество должно быть целым числом больше 0")
        else:
            print("Такого товара нет на складе")

    def show_items(self):
        for item, quantity in self.storage.items():
            print(f"{item} - {quantity} шт.")


# Пример использования и результат

printer = Printer("Canon Pixma", 5000, 3, "струйная")
scanner = Scanner("HP Scanjet", 8000, 2.5, "1200 dpi")
xerox = Xerox("Xerox WorkCentre", 15000, 20, 30)

warehouse = Warehouse()
warehouse.add_item(printer, 10)
warehouse.add_item(scanner, 5)
warehouse.add_item(xerox, 2)

# Canon Pixma: 5000 руб., 3 кг, технология печати: струйная - 10 шт.
# HP Scanjet: 8000 руб., 2.5 кг, разрешение сканирования: 1200 dpi - 5 шт.
# Xerox WorkCentre: 15000 руб., 20 кг, скорость копирования: 30 страниц/мин - 2 шт.
warehouse.show_items()

warehouse.remove_item(printer, 2)
warehouse.remove_item(scanner, "abc") # Количество должно быть целым числом больше 0
warehouse.remove_item(xerox, 5) # На складе недостаточно товара

warehouse.show_items()
# Canon Pixma: 5000 руб., 3 кг, технология печати: струйная - 8 шт.
# HP Scanjet: 8000 руб., 2.5 кг, разрешение сканирования: 1200 dpi - 5 шт.
# Xerox WorkCentre: 15000 руб., 20 кг, скорость копирования: 30 страниц/мин - 2 шт.
