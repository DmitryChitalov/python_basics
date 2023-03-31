#  Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
#  А также класс «Оргтехника», который будет базовым для классов-наследников.
#  Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
#  В базовом классе определите параметры, общие для приведённых типов.
#  В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

#  Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
#  Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).


# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП
class Warehouse:
    def __init__(self, location):
        self.location = location
        self.equipment = []

    def add_equipment(self, equipment):
        self.equipment.append(equipment)

    def remove_equipment(self, equipment):
        if equipment in self.equipment:
            self.equipment.remove(equipment)

    def get_all_equipment(self):
        return self.equipment


class OfficeEquipment:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_price(self):
        return self.price


class Printer(OfficeEquipment):
    def __init__(self, brand, model, price, color):
        super().__init__(brand, model, price)
        self.color = color

    def get_color(self):
        return self.color


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, price, resolution):
        super().__init__(brand, model, price)
        self.resolution = resolution

    def get_resolution(self):
        return self.resolution


class Xerox(OfficeEquipment):
    def __init__(self, brand, model, price, speed):
        super().__init__(brand, model, price)
        self.speed = speed

    def get_speed(self):
        return self.speed

# 6 задание. Продолжение решения задачи со складом оргтехники с валидацией вводимых данных:

def add_equipment(self, eq):
    if eq.brand in self.equipment:
        self.equipment[eq.brand][eq.model] += 1
    else:
        self.equipment[eq.brand] = {eq.model: 1}

def remove_equipment(self, eq):
    if eq.brand in self.equipment and eq.model in self.equipment[eq.brand] and self.equipment[eq.brand][eq.model] > 0:
        self.equipment[eq.brand][eq.model] -= 1

def get_all_equipment(self):
    for brand, models in self.equipment.items():
        for model, count in models.items():
            print(f"{brand} {model}: {count}")

def receive_equipment(self, eq, quantity):
    if isinstance(quantity, int):
        if eq.brand in self.equipment:
            if eq.model in self.equipment[eq.brand]:
                self.equipment[eq.brand][eq.model] += quantity
            else:
                self.equipment[eq.brand][eq.model] = quantity
        else:
            self.equipment[eq.brand] = {eq.model: quantity}
    else:
        print("Error: quantity should be an integer")

def transfer_equipment(self, eq, quantity, department):
    if isinstance(quantity, int):
        if eq.brand in self.equipment and eq.model in self.equipment[eq.brand] and self.equipment[eq.brand][eq.model] >= quantity:
            self.equipment[eq.brand][eq.model] -= quantity
            if eq.brand in department.equipment:
                if eq.model in department.equipment[eq.brand]:
                    department.equipment[eq.brand][eq.model] += quantity
                else:
                    department.equipment[eq.brand][eq.model] = quantity
            else:
                department.equipment[eq.brand] = {eq.model: quantity}
        else:
            print("Error: not enough equipment on the warehouse")
    else:
        print("Error: quantity should be an integer")


# Добавим в класс Warehouse метод для проверки, что вводимое количество является целым числом
def validate_quantity(self, quantity):
    if not isinstance(quantity, int):
        print("Error: quantity should be an integer")
        return False
    return True


# Этот метод может использоваться в методах receive_equipment() и transfer_equipment() класса Warehouse, чтобы проверять, что переданный аргумент quantity является целым числом.

# Например, в методе receive_equipment() можно добавить проверку валидности quantity перед добавлением оборудования на склад:

def receive_equipment(self, eq, quantity):
    if self.validate_quantity(quantity):
        if eq.brand in self.equipment:
            if eq.model in self.equipment[eq.brand]:
                self.equipment[eq.brand][eq.model] += quantity
            else:
                self.equipment[eq.brand][eq.model] = quantity
        else:
            self.equipment[eq.brand] = {eq.model: quantity}

# Аналогично, в методе transfer_equipment() можно добавить проверку валидности quantity перед перемещением оборудования на другой склад:

def transfer_equipment(self, eq, quantity, department):
    if self.validate_quantity(quantity):
        if eq.brand in self.equipment and eq.model in self.equipment[eq.brand] and self.equipment[eq.brand][eq.model] >= quantity:
            self.equipment[eq.brand][eq.model] -= quantity
            if eq.brand in department.equipment:
                if eq.model in department.equipment[eq.brand]:
                    department.equipment[eq.brand][eq.model] += quantity
                else:
                    department.equipment[eq.brand][eq.model] = quantity
            else:
                department.equipment[eq.brand] = {eq.model: quantity}
        else:
            print("Error: not enough equipment on the warehouse")


def validate_quantity(self, quantity):
    if not isinstance(quantity, int):
        print("Error: quantity should be an integer")
        return False
    return True

# создание склада
warehouse = Warehouse('Москва')

# создание оргтехники и добавление на склад
printer1 = Printer('Epson', 'L805', 20000, 'Цветной')
warehouse.add_equipment(printer1)

scanner1 = Scanner('Canon', 'CanoScan Lide 300', 5000, 2400)
warehouse.add_equipment(scanner1)

xerox1 = Xerox('HP', 'LaserJet Pro MFP M428fdw', 50000, True)
warehouse.add_equipment(xerox1)

# получение списка всего оборудования на складе
all_equipment = warehouse.get_all_equipment()
for equipment in all_equipment:
    print(type(equipment).__name__, equipment.get_brand(), equipment.get_model(), equipment.get_price())

# удаление оборудования со склада
warehouse.remove_equipment(printer1)

# получение списка оборудования на складе после удаления
all_equipment = warehouse.get_all_equipment()
for equipment in all_equipment:
    print(type(equipment).__name__, equipment.get_brand(), equipment.get_model(), equipment.get_price())

