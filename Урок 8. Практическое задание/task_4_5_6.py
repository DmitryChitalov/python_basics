"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). printer scanner xerox
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


class NotNumbersOwn(Exception):
    def __init__(self, text):
        self.text = text


class Storage:
    def __init__(self):
        self.__storage_area = []
        self.__journal = []

    def put_to_storage(self, item, count):
        for n in range(count):
            self.__storage_area.append(item)

    def get_storage(self):
        print(f"На складе '{len(self.__storage_area)}' единицы товара:")
        for key, i in enumerate(self.__storage_area, 1):
            print(key, i)

    def move_to_dep(self, item_id, dep_name):
        try:
            item = self.__storage_area.pop(item_id)
            print(f"{item} был передан в подразделение '{dep_name}'")
        except IndexError as err:
            print(f"{err}")


class OfficeEquipment:
    def __init__(self, voltage, weight):
        self.voltage = voltage
        self.weight = weight


class Printer(OfficeEquipment):
    def __init__(self, voltage, weight, paper_capacity, is_color):
        super().__init__(voltage, weight)
        self.paper_capacity = paper_capacity
        self.is_color = is_color

    def __str__(self):
        return f"Printer (voltage: {self.voltage}," \
               f" weight: {self.weight}," \
               f"paper_capacity: {self.paper_capacity}," \
               f"is_color: {self.is_color})"


class Scanner(OfficeEquipment):
    def __init__(self, voltage, weight, height):
        super().__init__(voltage, weight)
        self.height = height

    def __str__(self):
        return f"Scanner (voltage: {self.voltage}," \
           f" weight: {self.weight}," \
           f"height: {self.height})"


class Xerox(OfficeEquipment):
    def __init__(self, voltage, weight, print_width):
        super().__init__(voltage, weight)
        self.print_width = print_width

    def __str__(self):
        return f"Xerox (voltage: {self.voltage}," \
           f" weight: {self.weight}," \
           f"print_width: {self.print_width})"


my_printer = Printer(220, 210, 1000, True)
my_scanner = Scanner(220, 210, 400)
my_xerox = Xerox(220, 210, 297)
my_xerox_2 = Xerox(220, 140, 297)

my_storage = Storage()


try:
    line = input("Введите количество техники, которую нужно отправить на склад: ")

    if line.isnumeric():
        my_storage.put_to_storage(my_printer, int(line))
        my_storage.put_to_storage(my_scanner, int(line))
        my_storage.put_to_storage(my_xerox, int(line))
    else:
        raise NotNumbersOwn("Переданное значение не является числом")
except NotNumbersOwn as e:
    print(e)

my_storage.get_storage()
print()
my_storage.move_to_dep(0, 'Бухгалтерия')
my_storage.move_to_dep(1, 'Бухгалтерия')
print()
my_storage.get_storage()
