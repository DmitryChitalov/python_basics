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

class NoItemsExceptions(Exception):
    def __init__(self, txt):
        self.txt = txt


class PushPullDict:

    @staticmethod
    def push_items(first_items_dict, second_items_dict):
        """
        Добавление значений в словарь.
        Алгоритм в соответствии с ключем добавляет новые элеиенты или прибавляет соответствующее количество к уже существующим
        :param my_items_dict:
        :return:
        """
        if PushPullDict.check_correct(first_items_dict) and PushPullDict.check_correct(second_items_dict):
            for item in second_items_dict:
                if first_items_dict.get(item) == None:
                    first_items_dict[item] = second_items_dict[item]
                else:
                    first_items_dict[item] = first_items_dict[item] + second_items_dict[item]

            return first_items_dict
        else:
            return "Неверный формат входных данных"

    @staticmethod
    def pull_items(first_items_dict, second_items_dict):
        """
        Удаление значений из словаря.
        Алгоритм удаляет элементы, согласно списку second_items_dict
        При этом осуществляется проверка на существование и количество элементов
        :param my_items_dict:
        :return:
        """
        if PushPullDict.check_correct(first_items_dict) and PushPullDict.check_correct(second_items_dict):
            for item in second_items_dict:
                try:
                    if first_items_dict.get(item) == None:
                        raise NoItemsExceptions(f"На складе такой техники ({item}) нет!")
                    else:
                        curr_count = first_items_dict[item] - second_items_dict[item]
                        if curr_count < 0:
                            raise NoItemsExceptions(f"На складе такого количества техники ({item}) нет!")
                        else:
                            first_items_dict[item] = first_items_dict[item] - second_items_dict[item]
                            if first_items_dict[item] == 0:
                                del first_items_dict[item]

                except NoItemsExceptions as err:
                    print(err)

            return first_items_dict
        else:
            return "Неверный формат входных данных"

    @staticmethod
    def count_items(first_items_dict):
        """Подсчет количества позиций"""
        if PushPullDict.check_correct(first_items_dict):
            return sum(first_items_dict.values())
        else:
            return "Неверный формат входных данных"

    @staticmethod
    def check_correct(first_items_dict):
        """Проверка корректности заполнения словаря"""
        is_correct = False
        try:
            sum(first_items_dict.values())
            is_correct = True
        except:
            is_correct = False

        return is_correct


class Warehouse:
    max_input: int
    list_items: dict = {}

    def __init__(self, my_max_input):
        self.max_input = my_max_input
        self.list_items = {}

    def push_items(self, my_items_dict):
        if PushPullDict.check_correct(my_items_dict):
            try:
                tmp = PushPullDict.count_items(my_items_dict)
                if self.max_input - PushPullDict.count_items(self.list_items) - PushPullDict.count_items(
                        my_items_dict) >= 0:
                    PushPullDict.push_items(self.list_items, my_items_dict)
                    print(self.list_items)
                else:
                    raise NoItemsExceptions("На складе нет места для размещения указанной партии оргтехники.")
            except NoItemsExceptions as err:
                print(err)
        else:
            print("Неверный формат входных данных")

    def pull_items(self, my_items_dict):
        if PushPullDict.check_correct(my_items_dict):
            PushPullDict.pull_items(self.list_items, my_items_dict)
            print(self.list_items)
        else:
            print("Неверный формат входных данных")

    def count_items(self):
        return PushPullDict.count_items(self.list_items)


class Orgtehniks:
    model_name: str
    manufacturer_name: str

    def __init__(self, my_model_name, my_manufacturer_name):
        self.model_name = my_model_name
        self.manufacturer_name = my_manufacturer_name


class Printer(Orgtehniks):
    paper_count: int
    print_type: str
    print_speed: int

    def __init__(self, my_model_name, my_manufacturer_name, my_print_type, my_paper_count, my_print_speed):
        super().__init__(my_model_name, my_manufacturer_name)
        self.paper_count = my_paper_count
        self.print_type = my_print_type
        self.print_speed = my_print_speed


class Scanner(Orgtehniks):
    paper_size: str
    scan_speed: int

    def __init__(self, my_model_name, my_manufacturer_name, my_paper_size, my_scan_speed):
        super().__init__(my_model_name, my_manufacturer_name)
        self.paper_size = my_paper_size
        self.scan_speed = my_scan_speed


class Xerox(Orgtehniks):
    copy_speed: int

    def __init__(self, my_model_name, my_manufacturer_name, my_copy_speed):
        super().__init__(my_model_name, my_manufacturer_name)
        self.copy_speed = my_copy_speed


class Departament(Warehouse):
    name: str
    max_input = 100

    def __init__(self, my_name):
        self.name = my_name

# Проверка работы

# Объявление объектов оргтехники
my_printer1 = Printer("HPLJ", "HP", "Laser", 100, 10)
my_printer2 = Printer("HPDJ", "HP", "Inc", 100, 5)
my_scaner1 = Scanner("CanonA4", "Canon", "А4", 10)
my_scaner2 = Scanner("HPA3", "HP", "А3", 5)
my_xerox1 = Xerox("Xerox25", "Xerox", 25)
my_xerox2 = Xerox("Xerox50", "Xerox", 50)

# Объявление списков оргтехники для передачи на склад (они же - для передачи в отделы)
printers_dict = {my_printer1: 2, my_printer2: 3}
scanners_dict = {my_scaner1: 3, my_scaner2: 1}
xerox_dict = {my_xerox1: 1, my_xerox2: 1}

# Объявление склада и отделов
warenhouse_one = Warehouse(30)
warenhouse_two = Warehouse(30)

departament_one = Departament("ДИС")
departament_two = Departament("ДИТ")

# Заполнение склада
warenhouse_one.push_items(printers_dict)
warenhouse_one.push_items(printers_dict)
warenhouse_one.push_items(printers_dict)
warenhouse_one.push_items(scanners_dict)
warenhouse_one.push_items(xerox_dict)

warenhouse_two.push_items(printers_dict)
warenhouse_two.push_items(printers_dict)


print(f"На складе 1 {warenhouse_one.count_items()} объектов")
print(f"На складе 2 {warenhouse_two.count_items()} объектов")

warenhouse_one.pull_items(printers_dict)

print(f"На складе {warenhouse_one.count_items()} объектов")


#Передача техники отделам
warenhouse_one.pull_items(printers_dict)
departament_one.push_items(printers_dict)
print(f"На складе {warenhouse_one.count_items()} объектов")
print(f"В отделе 1 {departament_one.count_items()} объектов")

warenhouse_one.pull_items(printers_dict)
departament_two.push_items(printers_dict)
print(f"На складе {warenhouse_one.count_items()} объектов")
print(f"В отделе 2 {departament_two.count_items()} объектов")

