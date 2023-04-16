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

class Storage:
    def __init__(self, capacity):
        self._officeEquipments = []
        self._capacity = capacity


class OfficeEquipment:
    def __init__(self, price, articleNumber, name, department):
        self._price = price
        self._articleNumber = articleNumber
        self._name = name
        self.department = department

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def articleNumber(self):
        return self._articleNumber

    def printInfo(self):
        print(f"Department: {self.department}, Name: {self._name}, Price: {self._price}, Article number: {self._articleNumber}")

class Scanner(OfficeEquipment):
    def __init__(self, price, articleNumber, name, department, resolutionByX, resolutionByY):
        super().__init__(self, price, articleNumber, name, department)
        self._resolutionByX = resolutionByX
        self._resolutionByY = resolutionByY

    @property
    def resolutionByX(self):
        return self._resolutionByX

    @property
    def resolutionByY(self):
        return self._resolutionByY

    def printInfo(self):
        print(f"Department: {self.department}, Name: {self._name}, Price: {self._price}, Article number: {self._articleNumber}, resolution by X: {self.resolutionByX}, resolution by Y: {self.resolutionByY}")

class Printer(OfficeEquipment):
    def __init__(self, price, articleNumber, name, department, isBlackWhitePrinter, isLaserPrinter):
        super().__init__(self, price, articleNumber, name, department)
        self._isBlackWhitePrinter = isBlackWhitePrinter
        self._isLaserPrinter = isLaserPrinter

    @property
    def isBlackWhite(self):
        return self._isBlackWhitePrinter

    @property
    def isLaserPrinter(self):
        return self._isLaserPrinter

    def printInfo(self):
        print(f"Department: {self.department}, Name: {self._name}, Price: {self._price}, Article number: {self._articleNumber}, laser printer: {self.isLaserPrinter}, monochrome: {self.isBlackWhite}")


class Xerox(OfficeEquipment):
    def __init__(self, price, articleNumber, name, department, isBlackWhitePrinter, supportFax, isLaserXerox):
        super().__init__(self, price, articleNumber, name, department)
        self._isBlackWhitePrinter = isBlackWhitePrinter
        self._supportFax = supportFax
        self._isLaserXerox = isLaserXerox

    @property
    def isBlackWhite(self):
        return self._isBlackWhitePrinter

    @property
    def supportFax(self):
        return self._supportFax

    @property
    def isLaserXerox(self):
        return self._isLaserXerox

    def printInfo(self):
        print(f"Department: {self.department}, Name: {self._name}, Price: {self._price}, Article number: {self._articleNumber}, monochrome: {self.isBlackWhite}, laser xerox: {self.isLaserXerox}, support fax: {self.supportFax}")