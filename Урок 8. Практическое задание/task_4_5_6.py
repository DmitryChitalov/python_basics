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


class Stock:
    __stock_type = ["Printer", "Scaner", "Xerox"]
    __department = ["IT", "Security"]
    eq_vendors = []
    stock_count = {'Printer': 0, 'Scaner': 0, 'Xerox': 0}
    stock_department = [{'Department': "IT", 'Printer_count': 0, 'Scaner_count': 0, 'Xerox_count': 0},
                        {'Department': "Security", 'Printer_count': 0, 'Scaner_count': 0, 'Xerox_count': 0}]


class Equipment:
    equipment_count = 0
    equipment_vendors = []

    def __init__(self, eq_type, count, vendor):
        self.eq_type = eq_type
        self.count = count
        self.vendor = vendor

    def send_to_stock(self):
        Stock.eq_vendors.append(self.vendor)
        Stock.stock_count[self.eq_type] = Stock.stock_count[self.eq_type] + self.count


    def send_to_department(self, department, count_to_department):
        self.department = department
        self.count_to_department = count_to_department
        if department == "IT":
            if self.eq_type == "Printer":
                print("!!")
                Stock.stock_department[0]['Printer_count'] = Stock.stock_department[0][
                                                                 'Printer_count'] + count_to_department
                Stock.stock_count['Printer'] = Stock.stock_count['Printer'] - count_to_department
            if self.eq_type == "Scaner":
                Stock.stock_department[0]['Scaner_count'] = Stock.stock_department[0][
                                                                'Scaner_count'] + count_to_department
                Stock.stock_count['Scaner_count'] = Stock.stock_count['Scaner'] - count_to_department
            if self.eq_type == "Xerox":
                Stock.stock_department[0]['Xerox_count'] = Stock.stock_department[0][
                                                               'Xerox_count'] + count_to_department
                Stock.stock_count['Xerox'] = Stock.stock_count['Xerox'] - count_to_department
        if department == "Security":
            if self.eq_type == "Printer":
                Stock.stock_department[1]['Printer_count'] = Stock.stock_department[0][
                                                                 'Printer_count'] + count_to_department
                Stock.stock_count['Printer'] = Stock.stock_count['Printer'] - count_to_department
            if self.eq_type == "Scaner":
                Stock.stock_department[1]['Scaner_count'] = Stock.stock_department[0][
                                                                'Scaner_count'] + count_to_department
                Stock.stock_count['Scaner'] = Stock.stock_count['Scaner'] - count_to_department
            if self.eq_type == "Xerox":
                Stock.stock_department[1]['Xerox_count'] = Stock.stock_department[0][
                                                               'Xerox_count'] + count_to_department
                Stock.stock_count['Xerox'] = Stock.stock_count['Xerox'] - count_to_department


class Printer(Equipment):
    def __init__(self, eq_type, count, vendor, printer_model):
        super().__init__(eq_type, count, vendor)
        self.printer_type = printer_model


class Scaner(Equipment):
    def __init__(self, eq_type, count, vendor, scaner_model):
        super().__init__(eq_type, count, vendor)
        self.scaner_type = scaner_model


class Xerox(Equipment):
    def __init__(self, eq_type, xerox_model):
        super().__init__(eq_type, count, vendor)
        self.xerox_type = xerox_model


class MyError(Exception):
    def __init__(self, parm_1):
        self.message = parm_1


eq_type = input("Выберите тип устройства (Printer, Scaner,Xerox): ")
count = input("Введите количество устройств: ")
try:
    if not count.isnumeric():
        raise MyError("Ошибка введенных данных")
except MyError as err:
    print(err)

vendor = input("Введите название вендора: ")
eq_model = input("Введите модель устройства: ")
department = input("Выберите подразделение (IT или Security): ")
eq_count = input("Введите количество устройств для предачи в подразделение: ")
try:
    if not eq_count.isnumeric():
        raise MyError("Ошибка введенных данных")
except MyError as err:
    print(err)

if eq_type == "Printer":
    printers = Printer(eq_type, int(count), vendor, eq_model)
    printers.send_to_stock()
    printers.send_to_department(department, int(eq_count))
elif eq_type == "Scaner":
    scaners = Printer(eq_type, int(count), vendor, eq_model)
    scaners.send_to_stock()
    scaners.send_to_department(department, int(eq_count))
elif eq_type == "Xerox":
    xeroxs = Printer(eq_type, int(count), vendor, eq_model)
    xeroxs.send_to_stock()
    xeroxs.send_to_department(department, int(eq_count))

print(Stock.stock_department)
print(Stock.stock_count)
print(Stock.eq_vendors)

