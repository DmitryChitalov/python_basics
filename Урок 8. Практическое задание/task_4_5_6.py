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


class OwnError(Exception):
    pass


class Sklad:

    @staticmethod
    def input_data():
        while True:
            try:
                select = input(
                    "Выберите вид техники, который будем отгружать на склад (1 - принтер, 2 - сканер, 3 - ксерокс): ")
                if select.isnumeric() is False:
                    raise OwnError("Необходимо вводить цифры")
                elif int(select) > 3 or int(select) < 1:
                    print("Некорректный выбор, попробуйте ещё")
                    continue
                else:
                    select = int(select)
                    break
            except OwnError as err:
                print(err)
        return select


class OfficeEquipment:
    def __init__(self, model, color):
        self.model = model
        self.color = color


class Printer(OfficeEquipment):
    printer_list = {}
    counter = 1

    def __init__(self, model, color):
        super().__init__(model, color)
        self.printer_list[Printer.counter] = {"model": model, "color": color}
        Printer.counter += 1

    @staticmethod
    def to_print():
        print("Напечатал")

    def __str__(self):
        return f"Принтеры на складе: {self.printer_list}"


class Scaner(OfficeEquipment):
    printer_list = {}
    counter = 1

    def __init__(self, model, color):
        super().__init__(model, color)
        self.printer_list[Scaner.counter] = {"model": model, "color": color}
        Scaner.counter += 1

    @staticmethod
    def to_scan():
        print("Отсканировал")

    def __str__(self):
        return f"Сканеры на складе: {self.printer_list}"


class Xerox(OfficeEquipment):
    printer_list = {}
    counter = 1

    def __init__(self, model, color):
        super().__init__(model, color)
        self.printer_list[Xerox.counter] = {"model": model, "color": color}
        Xerox.counter += 1

    @staticmethod
    def to_copy():
        print("Скопировал")

    def __str__(self):
        return f"Ксероксы на складе: {self.printer_list}"


sklad = Sklad.input_data()

if sklad == 1:
    while True:
        a = Printer(model=input("Введите модель: "), color=input("Введите цвет: "))
        check = input("Продолжить заполнение склада? (y/n): ")
        if check.find("n") != -1:
            print(a)
            break
elif sklad == 2:
    while True:
        b = Scaner(model=input("Введите модель: "), color=input("Введите цвет: "))
        check = input("Продолжить заполнение склада? (y/n): ")
        if check.find("n") != -1:
            print(b)
            break
elif sklad == 3:
    while True:
        c = Xerox(model=input("Введите модель: "), color=input("Введите цвет: "))
        check = input("Продолжить заполнение склада? (y/n): ")
        if check.find("n") != -1:
            print(c)
            break
