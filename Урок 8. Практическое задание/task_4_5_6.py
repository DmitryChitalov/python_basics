class Warehouse:
    def __init__(self):
        self.inventory = []
    def add_item(self, item):
        self.inventory.append(item)
    def remove_item(self, item):
        self.inventory.remove(item)

class OfficeEquipment:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

class Printer(OfficeEquipment):
    def __init__(self, brand, model, price, print_speed):
        super().__init__(brand, model, price)
        self.print_speed = print_speed

class Scanner(OfficeEquipment):
    def __init__(self, brand, model, price, resolution):
        super().__init__(brand, model, price)
        self.resolution = resolution


class Xerox(OfficeEquipment):
    def __init__(self, brand, model, price, copying_speed):
        super().__init__(brand, model, price)
        self.copying_speed = copying_speed

warehouse = Warehouse()

# Создаем оргтехнику разных типов
printer = Printer("HP", "LaserJet", 200, "20 ppm")
scanner = Scanner("Epson", "Perfection", 150, "1200 dpi")
xerox = Xerox("Canon", "ImageRunner", 500, "50 cpm")

# Добавляем оргтехнику на склад
warehouse.add_item(printer)
warehouse.add_item(scanner)
warehouse.add_item(xerox)

# Удаляем оргтехнику со склада
warehouse.remove_item(printer)

# Выводим информацию
for item in warehouse.inventory:
    print(f"{item.brand} {item.model} - Цена: {item.price}")
    if isinstance(item, Printer):
        print(f"Скорость печати: {item.print_speed}")
    elif isinstance(item, Scanner):
        print(f"Разрешение: {item.resolution}")
    elif isinstance(item, Xerox):
        print(f"Скорость копирования: {item.copying_speed}")
    print()
