class StoreHouse:
    pass

class OfficeEquipment:
    def __init__(self, power_unit, interface, color):
        self.power_unit = power_unit
        self.interface = interface
        self.color = color

class Printer(OfficeEquipment):
    def __init__(self, power_unit, interface, color, speed_print):
        OfficeEquipment.__init__(self, power_unit, interface, color)
        self.speed_print = speed_print

class Scaner(OfficeEquipment):
    def __init__(self, power_unit, interface, color, speed_scan):
        OfficeEquipment.__init__(self, power_unit, interface, color)
        self.speed_scan = speed_scan

class Copier(OfficeEquipment):
    def __init__(self, power_unit, interface, color, speed_copi):
        OfficeEquipment.__init__(self, power_unit, interface, color)
        self.speed_copi = speed_copi

