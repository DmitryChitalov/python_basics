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

6. Продолжить работу над пятым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class Warehouse:
    def __init__(self, input_dict):
        self.inventory = input_dict


class OfficeEquip:
    paper_class = "white"
    interface = "USB"


class Printer(OfficeEquip):
    model = dict()

    def __init__(self, inp_dict):
        for key, val in inp_dict.items():
            val.extend([super().paper_class, super().interface])
            self.model[key] = val

    def __str__(self):
        return f"Добавлены на склад принтеры: {self.model}"


class Scanner(OfficeEquip):
    model = dict()

    def __init__(self, inp_dict):
        for key, val in inp_dict.items():
            val.extend([super().paper_class, super().interface])
            self.model[key] = val

    def __str__(self):
        return f"Добавлены на склад сканеры: {self.model}"


class Xerox(OfficeEquip):
    model = dict()

    def __init__(self, inp_dict):
        for key, val in inp_dict.items():
            val.extend([super().paper_class, super().interface])
            self.model[key] = val

    def __str__(self):
        return f"Добавлены на склад ксероксы: {self.model}"


class TypeCheck(Exception):
    def __init__(self, msg):
        self.msg = msg


"""Функция ввода данных"""


def input_data():

    res_dict = dict()

    while True:  # выполняем пока не найдём условие прерывания
        try:
            print("1.Принтеры\n"
                  "2.Cканеры\n"
                  "3.Ксероксы")
            select = input("Выберите вид техники который будем отгружать на склад, введите 1, 2 или 3: ")
            if select.isnumeric() is False:  # если не цифра, то вызываем ошибку
                raise TypeCheck("Необходимо вводить цифры")
            elif int(select) > 3 or int(select) < 1:
                print("Не корректный выбор, попробуйте ещё")
                continue
            else:
                select = int(select)
                break
        except TypeCheck as err:
            print(err)

    while True:
        key = input('Введите модель техники: ')
        res_list = list()
        inp_value = input('Введите формат бумаги: ')
        res_list.append(inp_value)
        inp_value = input('Введите бренд: ')
        res_list.append(inp_value)
        while True:
            try:
                inp_value = input('Введите количество техники: ')
                if inp_value.isnumeric() is False:  # если не цифра, то вызываем ошибку
                    raise TypeCheck("Необходимо вводить цифры")
                else:
                    res_list.append(inp_value)
                    break
            except TypeCheck as err:
                print(err)
        res_dict[key] = res_list
        check = input("Продолжаем пополнять текущий склад? (д/н): ")
        if check.find("н") != -1 or check.find("n") != -1:  # ищем символ "н" или "n" в строке, если есть то
            print("Пополнение склада закончено")
            break  # выходим из цикла
    return select, res_dict


"""Ввод данных о технике которой пополняем склад"""
select_warehouse, dict_technic = input_data()
"""В зависимости от выбранного вида техники пополняем нужный склад"""
if select_warehouse == 1:
    info_print = Printer(dict_technic)
    print(info_print)
elif select_warehouse == 2:
    info_print = Scanner(dict_technic)
    print(info_print)
elif select_warehouse == 3:
    info_print = Xerox(dict_technic)
    print(info_print)
