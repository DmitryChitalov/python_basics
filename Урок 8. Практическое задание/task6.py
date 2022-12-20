class StoreHouse:
    store_list = []

class OfficeEquipment:
    def __init__(self, power_unit, interface, color):
       self.power_unit = power_unit
       self.interface = interface
       self.color = color

    department_list = []

    def move_to(self, site, unit):
        try:
            if isinstance(self.power_unit, bool):
                if isinstance(self.interface, str):
                    if isinstance(self.color, str):
                        if site == "StoreHouse":
                            if [site, unit] in self.department_list:
                                self.department_list.remove([site, unit])
                            StoreHouse.store_list.append(unit)
                        else:
                            if unit in StoreHouse.store_list:
                                StoreHouse.store_list.remove(unit)
                            self.department_list.append([site, unit])
                    else:
                        raise ValueError("Цвет должен быть записан как строка!")
                else:
                    raise ValueError("Интерфейс должен быть записан как строка!")
            else:
                raise ValueError("Наличие блока питания должно записываться как булево выражение!")
        except ValueError as ve:
            print(ve)

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

a = Printer(True, "usb", "green", 7)
a.move_to("StoreHouse", a)
print(StoreHouse.store_list)
print(a.department_list)
a.move_to("IT", a)
print(StoreHouse.store_list)
print(a.department_list)
b = Scaner(True, "usb", 5, 7)
b.move_to("StoreHouse", a)
print(StoreHouse.store_list)
print(a.department_list)