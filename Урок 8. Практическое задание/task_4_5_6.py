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

from abc import ABC, abstractmethod


class Storage:
    '''Склад оргтехники'''
    office_equipments = {'printers': 20, 'scanners': 20, 'xeroxes': 20}


class OfficeEquipment(ABC, Storage):
    '''Оргтехника'''
    _equipments = {'printers': 10, 'scanners': 10, 'xeroxes': 10}
    _gave_equipments = {'printers': 0, 'scanners': 0, 'xeroxes': 0}

    @abstractmethod
    def dispatch_to_office(self, action, num):
        """
        perform action to class method
        :param str action: @classmethod name
        :param int num: number of office equipment
        :return: tuple[bool, equipment balance]
        :rtype: tuple
        """
        pass

    @classmethod
    def get_equipment(cls, what, num):
        """
        get equipment
        :param str what: equipment name
        :param int num: How much equipment
        :return: tuple[bool, equipment balance]
        :rtype: tuple
        """
        if cls._is_num(num):
            w = cls._equipments.get(what)
            if w - num >= 0:
                cls._equipments[what] = cls._equipments[what] - num
                cls._gave_equipments[what] = num
                return True, cls._equipments[what]
            else:
                is_update, storage_balance = cls._update_equipment(what, abs(w - num))
                if is_update:
                    cls._equipments[what] = w + abs(w - num) - num
                    cls._gave_equipments[what] = num
                    return True, storage_balance
                else:
                    return False, storage_balance
        return False, cls._equipments[what]

    @classmethod
    def return_equipment(cls, what, num):
        """
        return equipment
        :param str what: equipment name
        :param int num: How much equipment
        :return: tuple[bool, equipment balance]
        :rtype: tuple
        """
        if cls._is_num(num):
            w = cls._equipments.get(what)
            if None in [w] or cls._gave_equipments[what] < num:
                return False, cls._equipments[what]
            cls._equipments[what] = cls._equipments[what] + num
            return True, cls._equipments[what]

    @staticmethod
    def _is_num(num):
        if type(num) == int:
            return True
        return False

    @staticmethod
    def _update_equipment(what, num):
        """
        update equipment
        :param str what: equipment name
        :param int num: How much equipment
        :return: tuple[bool, storage balance]
        :rtype: tuple
        """
        try:
            w = Storage.office_equipments.get(what)
            if w >= num:
                Storage.office_equipments[what] -= num
                return True, w - num
            else:
                return False, w
        except KeyError:
            return False, -1


class Printer(OfficeEquipment):
    '''принтер'''
    def __init__(self):
        self.printers = 0

    def dispatch_to_office(self, action, num):
        my_product = 'printers'
        action_creator = {
            'get_equipment': lambda a, b: OfficeEquipment.get_equipment(a, b),
            'return_equipment': lambda a, b: OfficeEquipment.return_equipment(a, b)
        }
        try:
            is_res, res = action_creator[action](my_product, num)
            if is_res and action == 'get_equipment':
                self.printers += num
                return True, res
            if is_res and action == 'return_equipment':
                self.printers -= num
                return is_res, res
            raise ValueError
        except ValueError:
            return False, -1
        except KeyError:
            return False, -1

    def __str__(self):
        return f"{self.printers}"


class Scanner(OfficeEquipment):
    '''сканер'''
    def __init__(self):
        self.scanners = 0

    def dispatch_to_office(self, action, num):
        my_product = 'scanners'
        action_creator = {
            'get_equipment': lambda a, b: OfficeEquipment.get_equipment(a, b),
            'return_equipment': lambda a, b: OfficeEquipment.return_equipment(a, b)
        }
        try:
            is_res, res = action_creator[action](my_product, num)
            if is_res and action == 'get_equipment':
                self.scanners += num
                return True, res
            if is_res and action == 'return_equipment':
                self.scanners -= num
                return is_res, res
            raise ValueError
        except ValueError:
            return False, -1
        except KeyError:
            return False, -1

    def __str__(self):
        return f"{self.scanners}"


class Xerox(OfficeEquipment):
    '''ксерокс'''
    def __init__(self):
        self.xeroxes = 0

    def dispatch_to_office(self, action, num):
        my_product = 'xeroxes'
        action_creator = {
            'get_equipment': lambda a, b: OfficeEquipment.get_equipment(a, b),
            'return_equipment': lambda a, b: OfficeEquipment.return_equipment(a, b)
        }
        try:
            is_res, res = action_creator[action](my_product, num)
            if is_res and action == 'get_equipment':
                self.xeroxes += num
                return True, res
            if is_res and action == 'return_equipment':
                self.xeroxes -= num
                return is_res, res
            raise ValueError
        except ValueError:
            return False, -1
        except KeyError:
            return False, -1

    def __str__(self):
        return f"{self.xeroxes}"


p = Printer()
s = Scanner()
x = Xerox()

print(p.dispatch_to_office('get_equipment', 5))
print(p.dispatch_to_office('return_equipment', 20))
print()

print(s.dispatch_to_office('get_equipment', 30))
print(s.dispatch_to_office('get_equipment', 31))
print()

print(x.dispatch_to_office('get_equipment', 2))
print(x.dispatch_to_office('get_equipment', 8))
print()

print(f"{p.printers=}, {s.scanners=}, {x.xeroxes=}")
print(f"{OfficeEquipment._equipments=}")
print(f"{Storage.office_equipments=}")
