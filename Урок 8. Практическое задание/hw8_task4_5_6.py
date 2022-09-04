class Warehouse:
    print("Склад оргтехники")

    storage = {}

    def __init__(self):
        self.storage = {'Printer': {}, 'Scaner': {}, 'Xerox': {}}
        pass

    @staticmethod
    def equip_add(equip, count):
        equip_type = equip.__class__.__name__
        try:
            Warehouse.storage[equip_type][equip.name] += count
        except KeyError:
            if equip_type not in Warehouse.storage:
                Warehouse.storage[equip_type] = {}
                Warehouse.storage[equip_type][equip.name] = count
            elif equip.name not in Warehouse.storage[equip_type]:
                Warehouse.storage[equip_type][equip.name] = count
        return

    def __str__(self):
        output = ''
        for key, value in Warehouse.storage.items():
            output += key
            print(value)
            for el, count in value.items():
                output += f'{el} {count}'
        return output


class Equip(Warehouse):
    def __init__(self, ser_num, prod, color, serv_life):
        super().__init__()
        self.ser_num = ser_num
        self.prod = prod
        self.name = color
        self.serv_life = serv_life


class Printer(Equip):
    total_print = 0

    def __init__(self, ser_num, prod, color, serv_life, print_type):
        super().__init__(ser_num, prod, color, serv_life)
        self.print_type = print_type
        Printer.total_print += 1


class Scanner(Equip):
    total_scan = 0

    def __init__(self, ser_num, prod, color, serv_life, scan_type):
        super().__init__(ser_num, prod, color, serv_life)
        self.scan_type = scan_type
        Scanner.total_scan += 1


class Xerox(Equip):
    total_xer = 0

    def __init__(self, ser_num, prod, color, serv_life, xer_type):
        super().__init__(ser_num, prod, color, serv_life)
        self.xer_type = xer_type
        Xerox.total_xer += 1


p1 = Printer(1, 'samsung', 'white', 10, 'струйный')
p2 = Scanner(2, 'canon', 'black', 7, 'планшетный')
p3 = Xerox(3, 'asus', 'grey', 8, 'цифровой')
p4 = Printer(4, 'lenovo', 'yellow', 13, 'лазерный')

war = Warehouse()
print("Всего принетров: ", Printer.total_print)
print("Всего сканнеров: ", Scanner.total_scan)
print("Всего сканнеров: ", Xerox.total_xer)

Warehouse.equip_add(p1, 10)
Warehouse.equip_add(p2, 20)
Warehouse.equip_add(p3, 5)
print(Warehouse.storage)
