class Equipmentwarehouse:
    a = []
    b = {}

    def a1(self, equipment):
        self.a.append(equipment)
        if self.b.get(equipment.t) is not None:
            self.b[equipment.t] += 1
        else:
            self.b.setdefault(equipment.t, 1)

    def b1(self):
        for item in self.a:
            print(item)

    def c1(self):
        for el, el2 in self.b.items():
            print(f"{el} - {el2}")


class OfficeEquipment:
    def __init__(self, t: str, manufacturer: str, cost: float):
        self.t = str(t)
        self.manufacturer = str(manufacturer)
        self.cost = float(cost)

    def __str__(self):
        return f"{self.t} {self.manufacturer}"


class Printer(OfficeEquipment):
    def __init__(self, manufacturer: str, cost: int, sheetsperminute: int):
        self.sheetsperminute = sheetsperminute
        super().__init__("Принтер", manufacturer, cost)


class Scanner(OfficeEquipment):
    def __init__(self, manufacturer: str, cost: int, scanningspeed: int):
        self.scanningspeed = scanningspeed
        super().__init__("Сканер", manufacturer, cost)


class Copier(OfficeEquipment):
    def __init__(self, manufacturer: str, cost: int, size: str):
        self.size = size
        super().__init__("Копер", manufacturer, cost)


if __name__ == '__main__':
    printer1 = Printer(f"Samsung S3000", 25000, 60)
    printer2 = Printer(f"Oki T47", 12000, 30)
    scanner1 = Scanner(f"Ricoh Coolscann", 15000, 20)
    scanner2 = Scanner(f"Lalel 6343", 9000, 18)
    copier1 = Copier(f"Kitford Ki123", 5000, "300х300")

    equipmentwarehouse = Equipmentwarehouse()
    equipmentwarehouse.a1(printer1)
    equipmentwarehouse.a1(printer2)
    equipmentwarehouse.a1(scanner1)
    equipmentwarehouse.a1(scanner2)
    equipmentwarehouse.a1(copier1)

    equipmentwarehouse.b1()
    equipmentwarehouse.c1()