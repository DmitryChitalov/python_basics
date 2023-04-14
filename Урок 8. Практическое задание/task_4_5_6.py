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
    def __init__(self, input_dict):
        self.inventory = input_dict


class Orgtech(Storage):
    paper_class = "A4"
    interface = "USB"


class Printer(Orgtech):
    model = dict()

    def __init__(self, inp_dict):
        for key, val in inp_dict.items():
            val.extend([super().paper_class, super().interface])
            self.model[key] = val

    def __str__(self):
        return f"Принтеры добавлены на склад: {self.model}"


class Scanner(Orgtech):
    model = dict()

    def __init__(self, inp_dict):
        for key, val in inp_dict.items():
            val.extend([super().paper_class, super().interface])
            self.model[key] = val

    def __str__(self):
        return f"Сканеры добавлены на склад: {self.model}"


class Xerox(Orgtech):
    model = dict()

    def __init__(self, inp_dict):
        for key, val in inp_dict.items():
            val.extend([super().paper_class, super().interface])
            self.model[key] = val

    def __str__(self):
        return f"Копировальные аппараты добавлены на склад ксероксы: {self.model}"


class TypeCheck(Exception):
    def __init__(self, msg):
        self.msg = msg


def reception():
    res_dict = dict()
    while True:  # выполняем пока не найдём условие прерывания
        try:
            select = input('Выберите тип оргтехники, которую будем отгружать на сколад:\n'
                           '1-Принтер, 2-Сканер, 3-Копировальный аппарат ')
            if select.isnumeric() is False:
                raise TypeCheck('Необходимо ввести цифры 1, 2 или 3')
            elif  3 < int(select) < 1:
                print("Не корректный выбор, попробуйте ещё")
                continue
            else:
                select = int(select)
                break
        except TypeCheck as err:
            print(err)

    while True:
        res_list = list()
        in_model = input('Введите модель: ')  # key
        in_sn = input('Введите s/n оборудования: ')
        res_list.append(in_sn)
        in_location = input('Введите локацию, откуда поступает оборудование: ')
        res_list.append(in_location)
        res_dict[in_model] = res_list
        check = input("Продолжаем пополнять текущий склад? (д/н): ")
        if check.find("н") != -1 or check.find("n") != -1:  # ищем символ "н" или "n" в строке, если есть то
            print("Пополнение склада закончено")
            break  # выходим из цикла
    return select, res_dict


"""Ввод данных о технике которой пополняем склад"""
select_storage, dict_orgtech = reception()
"""В зависимости от выбранного вида техники пополняем нужный склад"""
if select_storage == 1:
    info_print = Printer(dict_orgtech)
    print(info_print)
elif select_storage == 2:
    info_print = Scanner(dict_orgtech)
    print(info_print)
elif select_storage == 3:
    info_print = Xerox(dict_orgtech)
    print(info_print)
