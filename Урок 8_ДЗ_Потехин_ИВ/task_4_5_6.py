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


# создаем класс исключений (введено не число товара для передачи на склад)
class NotNumbersOwn(Exception):
    def __init__(self, text):
        self.text = text


# создаем класс "Склад"
class Stock:
    def __init__(self):
        self._stock_area = []


    # метод определяющий помещение техники на склад
    def put_to_stock(self, item, count):
        for n in range(count):
            self._stock_area.append(item)

    # метод определения количества товара на складе
    def get_stock(self):
        print(f"На складе '{len(self._stock_area)}' единицы товара:")
        for key, i in enumerate(self._stock_area, 1):
            print(key, i)

    # метод перемещения со склада в департамент организации
    def move_to_dep(self, item_id, dep_name):
        try:
            item = self._stock_area.pop(item_id)
            print(f"{item} был передан в подразделение '{dep_name}'")
        except IndexError as err:
            print(f"{err}")


# создаем класс офисной техники, задаем атрибуты системы питания и веса техники
class OfficeEquipment:
    def __init__(self, voltage, weight):
        self.voltage = voltage
        self.weight = weight


# создаем дочерний класс Принтеров
class Printer(OfficeEquipment):
    def __init__(self, voltage, weight, paper_capacity, is_color):
        super().__init__(voltage, weight)  # наследование от класса OfficeEquipment
        self.paper_capacity = paper_capacity  # добавляем атрибут емкости лотка бумаги
        self.is_color = is_color  # атрибут логический, цветной или нет

    def __str__(self):
        return f"Printer (voltage: {self.voltage}, weight: {self.weight}," \
               f"paper_capacity: {self.paper_capacity},is_color: {self.is_color})"


# создаем дочерний класс Сканеров
class Scanner(OfficeEquipment):
    def __init__(self, voltage, weight, height):
        super().__init__(voltage, weight)  # наследование от класса OfficeEquipment
        self.height = height

    def __str__(self):
        return f"Scanner (voltage: {self.voltage},weight: {self.weight},height: {self.height})"


# создаем дочерний класс Ксеросков
class Xerox(OfficeEquipment):
    def __init__(self, voltage, weight, print_width):
        super().__init__(voltage, weight)  # наследование от класса OfficeEquipment
        self.print_width = print_width  # атрибут ширины печати

    def __str__(self):
        return f"Xerox (voltage: {self.voltage}, weight: {self.weight}, print_width: {self.print_width})"


# клиентский код
# создаем объекты по дочерним классам оргтехники
my_printer = Printer(220, 210, 1000, True)
my_scanner = Scanner(220, 210, 400)
my_xerox = Xerox(220, 210, 297)
my_xerox_2 = Xerox(110, 140, 297)
# создаем объект класса склад
my_stock = Stock()
# заправщиваем ввод кол-ва товара
try:
    line = input("Введите количество техники каждого типа, которую нужно отправить на склад: ")
    # делаем проверку ввода числа
    if line.isnumeric():
        my_stock.put_to_stock(my_printer, int(line))
        my_stock.put_to_stock(my_scanner, int(line))
        my_stock.put_to_stock(my_xerox, int(line))
        my_stock.put_to_stock(my_xerox_2, int(line))
    else:
        # поднимаем метод исключения
        raise NotNumbersOwn("Переданное значение не является числом,программа прекращает работу!")
except NotNumbersOwn as e:
    print(e)
    quit()  # завершаем программу
# вывод на печать
my_stock.get_stock()
print()
# блок перемещений
my_stock.move_to_dep(0, 'Бухгалтерия')
my_stock.move_to_dep(2, 'Финансовый контроль')
my_stock.move_to_dep(3, 'Тех. блок')
my_stock.move_to_dep(7, 'Юридический отдел')
print()
# остаток на складе
print('Остаток на складе после перемеещения оборудования в департаменты организации:')
my_stock.get_stock()
