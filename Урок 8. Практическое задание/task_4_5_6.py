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
class EquipmentWarehouse:
    __repo = []
    __content = {}

    def receipt_equipment(self, technique):
        if not isinstance(technique, OfficeHardware):
            raise Exception("Принимаем только оргтехнику!!!")
        self.__repo.append(technique)
        if self.__content.get(technique.type) is not None:
            self.__content[technique.type] += 1
        else:
            self.__content.setdefault(technique.type, 1)

    def counting_items(self):
        for item in self.__repo:
            print(item)

    def counting(self):
        for a, b in self.__content.items():
            print(f"{a}: {b} шт")


class OfficeHardware:
    def __init__(self, type: str, model: str, price: float, sn: str):
        self.type = str(type)
        self.model = str(model)
        self.price = float(price)
        self.sn = str(sn)

    def __str__(self):
        return f"{self.type} {self.model}"


class Printer(OfficeHardware):
    def __init__(self, model: str, price: float, sn: str):
        super().__init__("Принтер", model, price, sn)


class Scanner(OfficeHardware):
    def __init__(self, model: str, price: float, sn: str):
        super().__init__("Сканер", model, price, sn)


class Xerox(OfficeHardware):
    def __init__(self, model: str, price: float, speed: int, sn: str):
        self.velocity = speed
        super().__init__("Ксерокс", model, price, sn)


if __name__ == "__main__":
    p1 = Printer("HP 2312dn", 7090, "N6SS549876548")
    s1 = Scanner("Pantum P2200", 6100.12, "3893745631FFF")
    s2 = Scanner("Xerox P3020", 5200.17, "5BB6542133")
    x1 = Xerox("Canon PIXMA G1411", 3509.54, 20, "BN8#SSSF")

    wh = EquipmentWarehouse()
    wh.receipt_equipment(p1)
    wh.receipt_equipment(s1)
    wh.receipt_equipment(s2)
    wh.receipt_equipment(x1)

    wh.counting_items()
    wh.counting()