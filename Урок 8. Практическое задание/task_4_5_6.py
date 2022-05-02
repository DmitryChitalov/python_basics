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

class Warehouse:
    __storage = []
    __summary = {}
    def push(self, equipment):
        if not isinstance(equipment, Equipment):
            raise Exception('Склад оргтехники')
        self.__storage.append(equipment)
        if self.__summary.get(equipment.type) is not None:
            self.__summary[equipment.type] += 1
        else:
            self.__summary.setdefault(equipment.type, 1)
    def report_items(self):
        for item in self.__storage:
            print(item)
    def report_total(self):
        for k, v in self.__summary.items():
            print(f'{k}: {v} шт')
class Equipment:
    def __init__(self, type: str, model: str, cost: float, sn: str):
        self.type = str(type)
        self.model = str(model)
        self.cost = float(cost)
        self.sn = str(sn)
    def __str__(self):
        return f"{self.type} {self.model}"
class Printer(Equipment):
    def __init__(self, model: str, cost: float, is_colorful: bool, sn: str):
        self.is_colorful = is_colorful
        super().__init__('Принтер', model, cost, sn)
class Scanner(Equipment):
    def __init__(self, model: str, cost: float, dpi: str, sn: str):
        self.dpi = dpi
        super().__init__('Сканер', model, cost, sn)
class MFU(Equipment):
    def __init__(self, model: str, cost: float, is_colorful: bool, dpi: str, velocity: int, sn: str):
        self.is_colorful = is_colorful
        self.dpi = dpi
        self.velocity = velocity
        super().__init__('МФУ', model, cost, sn)
if __name__ == '__main__':
    printer01 = Printer('Xerox Phaser 3020', 9499, False, 'SS54N69876548')
    printer02 = Printer('HP Laser 107wr', 12499, False, '64FG855SFG5')
    scanner01 = Scanner('Mustek A3 1200 S', 34999, '1200x1200', '23265481FF5')
    scanner02 = Scanner('Plustek OpticBook 4800', 55999, '1200x1200', '13313F131FF')
    mfu01 = MFU('HP LaserJet Pro 400 M428fdn', 54999, False, '1200x1200', 38, 'HHFG8#HF')
    mfu02 = MFU('Brother DCP-L2500DR', 255999, False, '2400x600', 26, '548529BB6133')
    mfu03 = MFU('HP LaserJet Pro MFP M28w', 21999, False, '600x600', 18, '4849BB658554')
    warehouse = Warehouse()
    warehouse.push(printer01)
    warehouse.push(printer02)
    warehouse.push(scanner01)
    warehouse.push(scanner02)
    warehouse.push(mfu01)
    warehouse.push(mfu02)
    warehouse.push(mfu03)
    warehouse.report_items()
    warehouse.report_total()
