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


class Utils:

    @staticmethod
    def check_count_attr(count):
        try:
            if type(count) != int:
                raise PositiveNumberError("Количество товара должно быть числом!")
            else:
                if count < 1:
                    raise PositiveNumberError("Количество товара должно быть больше нуля!")
        except PositiveNumberError as err:
            print(err)
            return False
        return True


class PositiveNumberError(Exception):
    def __init__(self, msg: str):
        self.msg: str = msg


class OfficeEquipment:
    _count: int = 0
    name: str = ""
    manufacturer: str = ""
    type_technique: str = ""
    paper_size: str = "A4"

    def __init__(self, name: str, manufacturer: str, type_technique: str, paper_size: str):
        self.name = name
        self.manufacturer = manufacturer
        self.type_technique = type_technique
        self.paper_size = paper_size

    def add_object(self, count: int):
        if not Utils.check_count_attr(count):
            return
        self._count += count
        return 0

    def remove_object(self, count: int):
        if not Utils.check_count_attr(count):
            return
        if self._count >= count:
            self._count -= count
            return self._count
        else:
            print(f"{self.manufacturer}/{self.name} нет на складе в таком количестве")
            return -1

    def __str__(self):
        return f"Название: {self.name}\n" \
               f"Производитель: {self.manufacturer}\n" \
               f"Тип устройства: {self.type_technique}\n" \
               f"Используемый размер бумаги: {self.paper_size}\n" \
               f"Количетво товара: {self._count}\n"

    def is_equal(self, other):
        return (self.name == other.name and self.manufacturer == other.manufacturer
                and self.type_technique == other.type_technique)


class Printer(OfficeEquipment):

    def __init__(self, name, manufacturer, paper_size):
        super().__init__(name, manufacturer, "printer", paper_size)
        self.print_speed: int = 1
        self.count_cartridge: int = 1


class Scanner(OfficeEquipment):

    def __init__(self, name, manufacturer, paper_size):
        super().__init__(name, manufacturer, "scanner", paper_size)
        self.dpi: int = 300
        self.scanner_type: str = "tablet"


class Xerox(OfficeEquipment):

    def __init__(self, name, manufacturer, paper_size):
        super().__init__(name, manufacturer, "xerox", paper_size)
        self.speed_copy: int = 18


class Stock:
    _storage: [OfficeEquipment]
    count_technique: int = 0
    __stock_count = 0

    @staticmethod
    def __add_stock():
        Stock.__stock_count += 1

    @staticmethod
    def __sub_stock():
        if Stock.__stock_count > 0:
            Stock.__stock_count -= 1

    def __init__(self, name):
        self.name = name
        Stock.__add_stock()
        self._storage = []

    def __del__(self):
        Stock.__sub_stock()

    def adoption(self, technique: OfficeEquipment, count: int = 1):
        if not Utils.check_count_attr(count):
            return
        '''is_added = False
        if len(self._storage) > 0:
            for el in self._storage:
                if el.is_equal(technique):
                    print(el)
                    el.add_object(count)
                    print(el)
                    is_added = True
        else:
            if not is_added:
                self._storage.append(technique)
                technique.add_object(count)'''
        self._storage.append(technique)
        technique.add_object(count)
        self.count_technique += count
        # print(f"Товар: {technique}"
        #       f"принят на склад\n")

    def send(self, other, technique: OfficeEquipment, count: int = 1):
        print()
        print("************************************")
        print("*   Перемещение на другой склад:   *")
        print("************************************")
        print()
        if not Utils.check_count_attr(count):
            return
        if technique.remove_object(count) >= 0:
            temp_storage = self._storage.copy()
            self._storage.clear()
            for el in temp_storage:
                if not el.is_equal(technique):
                    self._storage.append(el)
            self.count_technique -= count
            other.adoption(technique, count)
            print(f"####################################\n"
                  f"{technique} был направлен на склад {other.name} в количестве {count}\n"
                  f"####################################")

    def __str__(self):
        full_report_store = ""
        full_report_store += "\n\n===================================================================================\n"
        full_report_store += f"ВСЕГО СКЛАДОВ: {Stock.__stock_count}\n"
        full_report_store += f"Всего {self.count_technique} товаров на складе {self.name}"
        full_report_store += "\n===================================================================================\n\n"
        if len(self._storage) > 0:
            for el in self._storage:
                full_report_store += f"{el}\n" \
                                     f"-----------------------------\n"
        else:
            full_report_store += "Склад оргтехники пуст"
        full_report_store += "\n===================================================================================\n\n"
        return full_report_store


alser_kz = Stock("ALSER KZ")
mechta = Stock("МЕЧТА")

printer_1 = Printer("X510", "Canon", "A5")
alser_kz.adoption(printer_1)
printer_2 = Printer("X510", "HP", "A4")
alser_kz.adoption(printer_2)
printer_3 = Printer("X510", "Sony", "A5")
alser_kz.adoption(printer_3)
printer_4 = Printer("Xion", "Sandy", "A4")
alser_kz.adoption(printer_4, 5)
printer_5 = Printer("X751i", "Canon", "A4")
alser_kz.adoption(printer_5)
printer_6 = Printer("LaserJet", "Canon", "A4")
mechta.adoption(printer_6)
printer_7 = Printer("MonoColor", "Canon", "A5")
mechta.adoption(printer_7)
printer_8 = Printer("Fabia", "HP", "A5")
mechta.adoption(printer_8)

scanner_1 = Scanner("Fl-7700S", "Fujitsu", "A3")
mechta.adoption(scanner_1)
scanner_2 = Scanner("V850", "Epson", "A3")
mechta.adoption(scanner_2)
scanner_3 = Scanner("Fl-7700S", "Fujitsu", "A3")
mechta.adoption(scanner_3)
scanner_4 = Scanner("ADS-3000N", "Brother", "A4")
alser_kz.adoption(scanner_4, 3)
scanner_5 = Scanner("V850", "Epson", "A3")
alser_kz.adoption(scanner_5, 10)
scanner_6 = Scanner("Fl-7700S", "Fujitsu", "A3")
alser_kz.adoption(scanner_6)
scanner_7 = Scanner("ADS-3000N", "Brother", "A4")
alser_kz.adoption(scanner_7)

xerox_1 = Xerox("500", "Xerox", "A4")
alser_kz.adoption(xerox_1)
xerox_2 = Xerox("500", "Xerox", "A4")
mechta.adoption(xerox_2)
xerox_3 = Xerox("820", "Xerox", "A4")
mechta.adoption(xerox_3, 4)
xerox_4 = Xerox("6060", "Xerox", "A1")
alser_kz.adoption(xerox_4, 2)
xerox_5 = Xerox("820", "Xerox", "A4")
mechta.adoption(xerox_5)

# alser_kz.send(mechta, scanner_4, 'asdf')
# alser_kz.send(mechta, scanner_5, 4)
# alser_kz.send(mechta, xerox_4, -5)
# alser_kz.send(mechta, printer_4)

print(alser_kz)
print(mechta)
