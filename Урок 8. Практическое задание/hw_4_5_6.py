class Warehouse:
    def __init__(self):
        self.items = {}
        self.items_departments = {}

    def show(self):
        for item in self.items:
            q = self.items[item]
            print(f"Склад: sku: {item} quantity: {q}")
        for department in self.items_departments:
            d = self.items_departments[department]
            for sku in d:
                print(f"Департамент: {department} sku: {sku} quantity: {d[sku]}")

    def add_item(self, sku, quantity):
        if sku in self.items:
            new_quantity = self.items[sku] + quantity
        else:
            new_quantity = quantity
        self.items[sku] = new_quantity

    def add_item_department(self, department, sku, quantity):
        # print(item.sku)
        if sku in self.items:
            q = self.items[sku]
            if (q < quantity):
                print(f"Невозможно перенести {sku} количество {quantity} в департамент {department}. Остаток на складе: {q}")
                exit(0)
            else:
                if department in self.items_departments:
                    d = self.items_departments[department]
                    if sku in d:
                        new_quantity = d[sku] + quantity
                    else:
                        new_quantity = quantity
                    self.items_departments[department][sku] = new_quantity
                else:
                    self.items_departments[department] = {sku:quantity}
                self.items[sku] -= quantity
        else:
            print(f"Невозможно переместить товар. Нет такого товара на складе: {sku}")


class OfficeEquipment:
    def input_sku(self, my_type):
        self.my_type = my_type
        try:
            self.sku = input(f'Введите код товара: ')
            self.price = int(input(f'Введите цену: '))
        except ValueError:
            print('Не верно введены данные')
            print(f'Для выхода - Q, продолжение - Enter')
            q = input(f'---> ')
            if q != 'Q' and q != 'q':
                return OfficeEquipment.input_sku(self, self.my_type)
            else:
                exit(0)


class Printer(OfficeEquipment):
    def input_sku(self):
        super().input_sku("printer")
        try:
            self.is_color = int(input(f'Принтер цветной?(1/0): '))
        except ValueError:
            print('Не верно введены данные')
            print(f'Для выхода - Q, продолжение - Enter')
            q = input(f'---> ')
            if q != 'Q' and q != 'q':
                return Printer.input_sku(self)
            else:
                exit(0)
        print(f'Добавлен новый принтер {self.sku}')


class Scanner(OfficeEquipment):
    def input_sku(self):
        super().input_sku("scanner")
        try:
            self.dpi = int(input(f'Введите DPI: '))
        except ValueError:
            print('Не верно введены данные')
            print(f'Для выхода - Q, продолжение - Enter')
            q = input(f'---> ')
            if q != 'Q' and q != 'q':
                return Scanner.input_sku(self)
            else:
                exit(0)
        print(f'Добавлен новый сканнер {self.sku}')


class Xerox(OfficeEquipment):
    def input_sku(self):
        super().input_sku("xerox")
        try:
            self.xeroxSpeed = int(input(f'Введите скорость копирования в минуту: '))
        except ValueError:
            print('Не верно введены данные')
            print(f'Для выхода - Q, продолжение - Enter')
            q = input(f'---> ')
            if q != 'Q' and q != 'q':
                return Xerox.input_sku(self)
            else:
                exit(0)
        print(f'Добавлен новый сканнер {self.sku}')

w = Warehouse()
p1 = Printer()
p1.input_sku()
p2 = Printer()
p2.input_sku()
s1 = Scanner()
s1.input_sku()
x1 = Xerox()
x1.input_sku()

w.add_item(p1.sku, 5)
w.add_item(p1.sku, 7)
w.add_item(p2.sku, 3)
w.add_item(s1.sku, 12)
w.add_item(x1.sku, 2)

w.add_item_department("magaz1", p1.sku, 10)
w.add_item_department("magaz2", p2.sku, 1)
w.show()