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


class OfficeInventorization:
    """Класс инвентаризации офисного оборудования"""

    def __init__(self, warehouse) -> None:
        self.__warehouse = warehouse
        self.__departments = {}

    def pickup_to_use(self, inv_id, department):
        """передача оборудования в пользование подразделением"""
        equipment = self.__warehouse.remove_equipment(inv_id)
        if equipment is None:
            raise ValueError(f"оборудование с инвентарным номером {inv_id} отсутствует на сладе")
        if department not in self.__departments:
            self.__departments[department] = []
        self.__departments[department].append(equipment)

    def return_to_warehouse(self, inv_id):
        """возврат оборудования на склад"""
        use_eq = self.find_equipment(inv_id)
        if use_eq is None:
            raise ValueError(f"оборудование с инвентарным номером {inv_id} не найдено")
        self.__warehouse.add_equipment(use_eq["equipment"])
        self.__delete_form_department(use_eq["department"], use_eq["equipment"])

    def find_equipment(self, inv_id):
        """
        ищет оборудование используемое подразделением
        :return: {"department": key, "equipment": equipment} | None
        """
        for key, value in self.__departments.items():
            for equipment in value:
                if equipment.inv_id == inv_id:
                    return {"department": key, "equipment": equipment}
        return None

    def get_equipment(self, department):
        """возвращает список оборудования для подразделения"""
        if department not in self.__departments:
            return []
        return self.__departments[department]

    def __delete_form_department(self, department, equipment):
        self.__departments[department].remove(equipment)
        if len(self.__departments[department]) == 0:
            del self.__departments["department"]


class OfficeWarehouse:
    """Склад оргтехники"""
    def __init__(self) -> None:
        self.__items = []

    def add_equipment(self, equipment):
        """добавляет оборудование на склад"""
        if self.get_by_id(equipment.inv_id) is not None:
            raise ValueError(f"оборудование с инвентарным номером "
                             f"{equipment.inv_id} уже добавлено")
        already = self.find_by_serial(equipment.serial_no)
        if already is not None:
            raise ValueError(f"серийны номер {equipment.serial_no} уже принадлежит "
                             f"оборудованию с номером {already.inv_id}")

        self.__items.append(equipment)

    def remove_equipment(self, inv_id):
        """
        удаляет оборудование с указанным инвентарным номером
        :return: удаляемый OfficeEquipment или None если таковой отсутвует
        """
        equipment = self.get_by_id(inv_id)
        if equipment is None:
            return None
        self.__items.remove(equipment)
        return equipment

    def get_by_id(self, inv_id):
        """
        возвращает оборудование по инвентарному номеру
        :return: OfficeEquipment | None
        """
        for item in self.__items:
            if item.inv_id == inv_id:
                return item
        return None

    def find_by_serial(self, serial_no):
        """
        ищет оборудование с указанным сериным номером
        :return: OfficeEquipment | None
        """
        for item in self.__items:
            if item.serial_no == serial_no:
                return item
        return None

    def __str__(self) -> str:
        result = "Склад(\n"
        for item in self.__items:
            result += f"\t{item}\n"
        result += ")"
        return result


class OfficeEquipment:
    """
    базовый класс оборудования
    """
    def __init__(self, inv_id, model, serial_no) -> None:
        self.__inv_id = inv_id
        self.__model = model
        self.__serial_no = serial_no

    @property
    def inv_id(self):
        """инвентарный номер"""
        return self.__inv_id

    @property
    def model(self):
        """модель устройства"""
        return self.__model

    @property
    def serial_no(self):
        """серийный номер"""
        return self.__serial_no

    def __str__(self) -> str:
        return f"{self.inv_id}, {self.model}, {self.serial_no}"


class Printer(OfficeEquipment):
    """класс офисной техники: принтеры"""
    TYPE_LASER = "laser"
    TYPE_MFU = "mfu"
    TYPE_INK = "ink"

    def __init__(self, inv_id, model, serial_no, ptype) -> None:
        super().__init__(inv_id, model, serial_no)
        self.ptype = ptype

    @property
    def ptype(self):
        """тип принтера"""
        return self.__ptype

    @ptype.setter
    def ptype(self, ptype):
        if ptype not in (Printer.TYPE_LASER, Printer.TYPE_INK, Printer.TYPE_MFU):
            raise AttributeError(f"неизвестный тип принтера: {ptype}")
        self.__ptype = ptype

    def __str__(self) -> str:
        return f"Принтер ({super().__str__()}, {self.__ptype})"


class Monitor(OfficeEquipment):
    """класс офисной тезники: мониторы"""
    def __init__(self, inv_id, model, serial_no, screen_size) -> None:
        super().__init__(inv_id, model, serial_no)
        self.__screen_size = int(screen_size)

    @property
    def screen_size(self):
        """размер экрана в дюймах"""
        return self.__screen_size

    def __str__(self) -> str:
        return f"Монитор ({super().__str__()}, {self.screen_size}\")"


class Scanner(OfficeEquipment):
    """класс офисной тезники: сканеры"""
    def __init__(self, inv_id, model, serial_no, scan_resolution) -> None:
        super().__init__(inv_id, model, serial_no)
        self.__resolution = scan_resolution

    @property
    def __resolution(self):
        return self.__scan_resolution

    @__resolution.setter
    def __resolution(self, res):
        items = res.split("x")
        if len(items) != 2:
            raise ValueError("разрешение должно быть в формате 0000x0000")
        self.__scan_resolution = [int(items[0]), int(items[1])]

    @property
    def res_x(self):
        """разрешение по x"""
        return self.__resolution[0]

    @property
    def res_y(self):
        """разрешение по y"""
        return self.__resolution[1]

    def __str__(self) -> str:
        return f"Сканер ({super().__str__()}, {self.res_x}x{self.res_y} dpi)"


def print_department_equipments(dep_list, inv):
    """печатает список оборудования по подразделениям"""
    for dep in dep_list:
        print(f"{dep}:")
        eq_list = inv.get_equipment(dep)
        if len(eq_list) == 0:
            print("\tпусто")
        else:
            for eq_item in eq_list:
                print(f"\t{eq_item}")


ware_house = OfficeWarehouse()
ware_house.add_equipment(Printer("0001", "HP LaserJet 1100", "92343020932093", Printer.TYPE_LASER))
ware_house.add_equipment(Printer("0002", "HP LaserJet 1100", "05654320932093", Printer.TYPE_LASER))
ware_house.add_equipment(Printer("0003", "Canaon 3000", "15663232333dd2", Printer.TYPE_INK))
ware_house.add_equipment(Printer("0004", "Xerox Phaser 8124", "89999884", Printer.TYPE_MFU))
ware_house.add_equipment(Printer("0005", "Xerox Phaser 8124", "89999882", Printer.TYPE_MFU))
ware_house.add_equipment(Printer("0006", "Xerox Phaser 8124", "89999881", Printer.TYPE_MFU))
ware_house.add_equipment(Monitor("0070", "Dell E1722s", "755377737", 17))
ware_house.add_equipment(Monitor("0071", "Dell E1722s", "755377738", 17))
ware_house.add_equipment(Monitor("0072", "Dell E1722s", "755377739", 17))
ware_house.add_equipment(Monitor("0073", "Samsung SyncMaster 3NE", "111992992", 19))
ware_house.add_equipment(Monitor("0074", "Samsung SyncMaster 3NE", "112122122", 19))
ware_house.add_equipment(Monitor("0075", "Lenovo 2144", "9823-111-323", 21))
ware_house.add_equipment(Scanner("0106", "Avision FB10", "011011011", "600x600"))
ware_house.add_equipment(Scanner("0107", "Canon CanoScan LiDE 400", "01101188811", "4800x4800"))

print(f"\nДо распределения:\n{ware_house}")

departments = ("it", "accounting", "hr")
inventory = OfficeInventorization(ware_house)

print("\nВ пользовании:")
print_department_equipments(departments, inventory)

inventory.pickup_to_use("0001", "accounting")
inventory.pickup_to_use("0005", "accounting")
inventory.pickup_to_use("0006", "accounting")
inventory.pickup_to_use("0071", "accounting")
inventory.pickup_to_use("0004", "it")
inventory.pickup_to_use("0072", "it")
inventory.pickup_to_use("0074", "it")
inventory.pickup_to_use("0073", "it")
inventory.pickup_to_use("0107", "hr")
inventory.pickup_to_use("0075", "hr")
inventory.pickup_to_use("0002", "hr")

print(f"\nПосле распределения:\n{ware_house}")
print("\nВ пользовании:")
print_department_equipments(departments, inventory)

inventory.return_to_warehouse("0107")
inventory.return_to_warehouse("0073")

print(f"После возврвата:\n{ware_house}")
print("\nВ пользовании:")
print_department_equipments(departments, inventory)

removed = ware_house.remove_equipment("0073")
print(removed)
print(f"\nПосле списания:\n{ware_house}")

removed = ware_house.remove_equipment("0073")
print(removed is None)

print("Попытка добавления с уже существующим номером:")
try:
    ware_house.add_equipment(Printer("0003", "Brother", "0000000", Printer.TYPE_INK))
except ValueError as err:
    print(err)

print("Попытка добавления с уже существующим серийником:")
try:
    ware_house.add_equipment(Printer("0011", "Brother", "755377737", Printer.TYPE_INK))
except ValueError as err:
    print(err)
