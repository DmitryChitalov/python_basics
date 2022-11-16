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


class OfficeWarehouse:
    """Склад оргтехники"""
    def __init__(self) -> None:
        self.__items = []

    def add_equipment(self, equipment):
        """добавляет оборудование на склад"""
        if self.get_by_id(equipment.inv_id) is None:
            raise ValueError(f"оборудование с инвентарным номером {equipment.inv_id} уже добавлено")
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


class Monitor(OfficeEquipment):
    """класс офисной тезники: мониторы"""
    def __init__(self, inv_id, model, serial_no, screen_size) -> None:
        super().__init__(inv_id, model, serial_no)
        self.__screen_size = int(screen_size)

    @property
    def screen_size(self):
        """размер экрана в дюймах"""
        return self.__screen_size


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
