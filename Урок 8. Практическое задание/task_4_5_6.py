class Warehouses:
    def __init__(self):
        self.storage = []

    def input(self, item, count):
        for n in range(count):
            self.storage.append(item)

    def get_availability(self):
        print(f"На складе {len(self.storage)} единиц ТМЦ:")
        for key, i in enumerate(self.storage, 1):
            print(key, i)

    def output(self, item_id, depart):
        try:
            item = self.storage.pop(item_id)
            print(f"{item} передан в отдел: {depart}")
        except IndexError as err:
            print(f"{err}")


class OfficeEquipment(Warehouses):
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model


class Printer(OfficeEquipment):
    def __init__(self, manufacturer, model, color):
        super().__init__(manufacturer, model)
        self.color = color

    def __str__(self):
        return f"Printer (Производитель:{self.manufacturer}, " \
               f"Модель:{self.model}, " \
               f"Цветной:{self.color})"


class Scanner(OfficeEquipment):
    def __init__(self, manufacturer, model, auto_feed: bool):
        super().__init__(manufacturer, model)
        self.auto_feed = auto_feed

    def __str__(self):
        return f"Scanner (Производитель:{self.manufacturer}, " \
            f"Модель:{self.model}, " \
            f"Автоподача:{self.auto_feed}"


class Copyr(OfficeEquipment):
    def __init__(self, manufacturer, model, lan: bool):
        super().__init__(manufacturer, model)
        self.lan = lan

    def __str__(self):
        return f"Copyr (Производитель:{self.manufacturer}, " \
           f"Модель:{self.model}, " \
           f"Сетевой:{self.lan})"


item_1 = Printer("Pantum", "P2500", False)
item_2 = Scanner("HP", "Pro4500", True)
item_3 = Copyr("Canon", "2425", True)
item_4 = Printer("Pantum", "MFP2022", True)

company = Warehouses()


company.input(item_1, 2)
company.input(item_2, 1)
company.input(item_3, 2)
company.input(item_4, 1)

company.get_availability()
company.output(2, "Производство")
company.get_availability()
company.output(2, "Бухгалтерия")
company.get_availability()
