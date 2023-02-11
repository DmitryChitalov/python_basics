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
class OfficeEquipmentWarehouse:
    """Это Класс=склад оргтехники"""
    print("\nСклад оргтехники")


class OfficeEquipment:
    """Это= Базовый класс оргтехники"""
    def __init__(self, producer, color):
        self.producer = producer
        self.color = color


class Printer(OfficeEquipment):
    """Это=Класс принтер"""
    amount_pr = 0

    def __init__(self, producer, color, pr_type):
        super().__init__(producer, color)
        self.pr_type = pr_type
        Printer.amount_pr += 1

    @staticmethod
    def name():
        return "<<Принтер>>"

    def type_printer(self):
        return self.pr_type

    def __str__(self):
        return "\tпроизводитель: {} \tцвет: {}  \tцена принтера: {}".format(self.producer, self.color, self.pr_type)


class Scanner(OfficeEquipment):
    """Это = Класс сканер"""
    amount_sc = 0

    def __init__(self, producer, color, sc_sensor):
        super().__init__(producer, color)
        self.sc_sensor = sc_sensor
        Scanner.amount_sc += 1

    @staticmethod
    def name():
        return"<<Сканер>>"

    def type_sensor(self):
        return self.sc_sensor

    def __str__(self):
        return "\tпроизводитель: {} \tцвет: {} \tцена сенсора: {}".format(self.producer, self.color, self.sc_sensor)


class Xerox(OfficeEquipment):
    """Это= Класс ксерокс"""
    amount_x = 0

    def __init__(self, producer, color, xer_wi_fi):
        super().__init__(producer, color)
        self.xer_wi_fi = xer_wi_fi
        Xerox.amount_x += 1

    @staticmethod
    def name():
        return "<<Ксерокс>>"

    def wi_fi_module(self):
        return self.xer_wi_fi

    def __str__(self):
        return "\tпроизводитель: {} \tцвет: {}   \tWi-Fi цена: {}".format(self.producer, self.color, self.xer_wi_fi)

p = Printer('Canon', 'red', '5000')
p2 = Printer('LG', 'yellow', '6500')
print(p.name(), p.amount_pr, "шт")
print(p.__str__())
print(p2.__str__())

s = Scanner('Samsung', 'black', '8700')
print(s.name(), s.amount_sc, "шт")
print(s.__str__())

x = Xerox('HP', 'white', 'есть')
x2 = Xerox('Samsung', 'black', 'есть')
x3 = Xerox('Kodak', 'red', 'есть')
print(x.name(), x.amount_x, "шт")
print(x.__str__())
print(x2.__str__())
print(x3.__str__())
