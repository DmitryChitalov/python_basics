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

"""4"""


class Storage:
    def __init__(self, name):
        self.name = name


class OfficeEquipment:
    def __init__(self, model, paper_size, manufacturer, price):
        self.model = model
        self.paper_size = paper_size
        self.manufacturer = manufacturer
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, print_type, print_speed):
        self.print_type = print_type
        self.print_speed = print_speed


class Scanner(OfficeEquipment):
    def __init__(self, resolution):
        self.resolution = resolution


class Copier(OfficeEquipment):
    def __init__(self, copy_speed):
        self.copy_speed = copy_speed


"""5"""
import re


class Storage:
    # def __init__(self, name):
    #    self.name = name
    store_area = []
    overall = {}
    given = []
    store_name = {1: 'Склад', 2: 'Розница', 3: 'Опт'}

    def get_val(self, eq_type, value, st_number):
        for i in range(value):
            for findings in self.store_area:
                a = re.findall(r'\w+', findings)[0]
                if a == eq_type:
                    self.given.append([st_number, findings])
                    self.store_area.remove(findings)
                    self.overall[eq_type] -= 1
                    break

    def store_info(self, s_num):
        print(f'Отправлено в {s_num}: {self.store_name[s_num]} >> ')
        for findings in self.given:
            if findings[0] == s_num:
                print(findings[1])

    def value_info(self):
        for findings in self.store_area:
            print(findings)

    def find_info(self):
        for key, val in self.overall.items():
            print(f'{key}: {val} шт')


class Equipment:
    def __init__(self, type_eq, model, paper_size, manufacturer, price):
        self.type_eq = type_eq
        self.model = model
        self.paper_size = paper_size
        self.manufacturer = manufacturer
        self.price = price

    @staticmethod
    def control():
        while True:
            st_control = Storage()
            choice = input('Выход - Q/q, продолжить - Enter >> ')
            if choice in ('Q', 'q'):
                exit()
            choice = input('Перемещение на склад - W, в магазин - S, сводная информация - I >> ')
            if choice in ('W', 'w'):
                Equipment.entrance()
                st_control.value_info()
                st_control.find_info()
            elif choice in ('S', 's'):
                eq_type = str(input('\nТип оргтехники - Принтер/Сканер/Копир: '))
                # if eq_type not in ('Принтер', 'Сканер', 'Копир'):
                #    raise ErrorView('Вы ввели неверный тип оборудования')
                value = int(input('Количество: '))
                st_number = int(input('Номер магазина: '))
                st_control.get_val(eq_type, value, st_number)
                st_control.value_info()
                st_control.find_info()
            elif choice in ('I', 'i'):
                store_name = int(input('Номер магазина - от 1 до 3: '))
                # if store_name not in (1, 2, 3):
                #    raise ErrorView('Вы ввели неверный номер магазина')
                st_control.store_info(store_name)

    @staticmethod
    def entrance():
        try:
            type_eq = str(input('\nТип оргтехники - Принтер/Сканер/Копир: '))
            # if type_eq not in ('Принтер', 'Сканер', 'Копир'):
            #    raise ErrorView('Неверный тип')
            if type_eq == 'Принтер':
                model = str(input('Модель: '))
                paper_size = str(input('Размер бумаги: '))
                manufacturer = str(input('Производитель: '))
                price = float(input('Цена: '))
                print_type = str(input('Тип печати /м-матричный, л-лазерный, с-струйный/: '))
                # if print_type not in ('м', 'л', 'с'):
                #    raise ErrorView('Неверный тип печати')
                print_speed = int(input('Скорость печати (л/м): '))
                Storage.store_area.append(str(Printer(model, paper_size, manufacturer, price, print_type, print_speed)))
                # if Storage.overall.get(type_eq) is not None:
                #    Storage.overall[type_eq] += 1
                # else:
                #    Storage.overall.setdefault(type_eq, 1)
            elif type_eq == 'Сканер':
                model = str(input('Модель: '))
                paper_size = str(input('Размер бумаги: '))
                manufacturer = str(input('Производитель: '))
                price = float(input('Цена: '))
                resolution = int(input('Разрешение: '))
                Storage.store_area.append(str(Scanner(model, paper_size, manufacturer, price, resolution)))
                # if Storage.overall.get(type_eq) is not None:
                #    Storage.overall[type_eq] += 1
                # else:
                #    Storage.overall.setdefault(type_eq, 1)
            elif type_eq == 'Копир':
                model = str(input('Модель: '))
                paper_size = str(input('Размер бумаги: '))
                manufacturer = str(input('Производитель: '))
                price = float(input('Цена: '))
                copy_speed = str(input('Скорость копирования: '))
                Storage.store_area.append(str(Copier(model, paper_size, manufacturer, price, copy_speed)))
                # if Storage.overall.get(type_eq) is not None:
                #    Storage.overall[type_eq] += 1
                # else:
                #    Storage.overall.setdefault(type_eq, 1)
        except ValueError:
            print('Недопустимое значение!')
        except ErrorView as error:
            print(error)


class ErrorView(Exception):
    def __init__(self, txt):
        self.txt = txt


class Printer(Equipment):
    def __init__(self, model, paper_size, manufacturer, price, print_type, print_speed):
        super().__init__('Принтер', model, paper_size, manufacturer, price)
        self.print_type = print_type
        self.print_speed = print_speed


class Scanner(Equipment):
    def __init__(self, model, paper_size, manufacturer, price, resolution):
        super().__init__('Сканер', model, paper_size, manufacturer, price)
        self.resolution = resolution


class Copier(Equipment):
    def __init__(self, model, paper_size, manufacturer, price, copy_speed):
        super().__init__('Копир', model, paper_size, manufacturer, price)
        self.copy_speed = copy_speed


Equipment.entrance()
Equipment.control()

"""6"""
import re


class Storage:
    store_area = []
    overall = {}
    given = []
    store_name = {1: 'Склад', 2: 'Розница', 3: 'Опт'}

    def get_val(self, eq_type, value, st_number):
        for i in range(value):
            for findings in self.store_area:
                a = re.findall(r'\w+', findings)[0]
                if a == eq_type:
                    self.given.append([st_number, findings])
                    self.store_area.remove(findings)
                    self.overall[eq_type] -= 1
                    break

    def store_info(self, s_num):
        print(f'Отправлено в {s_num}: {self.store_name[s_num]} >> ')
        for findings in self.given:
            if findings[0] == s_num:
                print(findings[1])

    def value_info(self):
        for findings in self.store_area:
            print(findings)

    def find_info(self):
        for key, val in self.overall.items():
            print(f'{key}: {val} шт')


class Equipment:
    def __init__(self, type_eq, model, paper_size, manufacturer, price):
        self.type_eq = type_eq
        self.model = model
        self.paper_size = paper_size
        self.manufacturer = manufacturer
        self.price = price

    @staticmethod
    def control():
        while True:
            st_control = Storage()
            choice = input('Выход - Q/q, продолжить - Enter >> ')
            if choice in ('Q', 'q'):
                exit()
            choice = input('Перемещение на склад - W, в магазин - S, сводная информация - I >> ')
            if choice in ('W', 'w'):
                Equipment.entrance()
                st_control.value_info()
                st_control.find_info()
            elif choice in ('S', 's'):
                eq_type = str(input('\nТип оргтехники - Принтер/Сканер/Копир: '))
                if eq_type not in ('Принтер', 'Сканер', 'Копир'):
                    raise ErrorView('Неверный тип оргтехники')
                value = int(input('Количество: '))
                st_number = int(input('Номер магазина: '))
                st_control.get_val(eq_type, value, st_number)
                st_control.value_info()
                st_control.find_info()
            elif choice in ('I', 'i'):
                store_name = int(input('Номер магазина - от 1 до 3: '))
                if store_name not in (1, 2, 3):
                    raise ErrorView('Неверный номер магазина')
                st_control.store_info(store_name)

    @staticmethod
    def entrance():
        try:
            type_eq = str(input('\nТип оргтехники - Принтер/Сканер/Копир: '))
            if type_eq not in ('Принтер', 'Сканер', 'Копир'):
                raise ErrorView('Неверный тип')
            if type_eq == 'Принтер':
                model = str(input('Модель: '))
                paper_size = str(input('Размер бумаги: '))
                manufacturer = str(input('Производитель: '))
                price = float(input('Цена: '))
                print_type = str(input('Тип печати /м-матричный, л-лазерный, с-струйный/: '))
                if print_type not in ('м', 'л', 'с'):
                    raise ErrorView('Неверный тип печати')
                print_speed = int(input('Скорость печати (л/м): '))
                Storage.store_area.append(str(Printer(model, paper_size, manufacturer, price, print_type, print_speed)))
                if Storage.overall.get(type_eq) is not None:
                    Storage.overall[type_eq] += 1
                else:
                    Storage.overall.setdefault(type_eq, 1)
            elif type_eq == 'Сканер':
                model = str(input('Модель: '))
                paper_size = str(input('Размер бумаги: '))
                manufacturer = str(input('Производитель: '))
                price = float(input('Цена: '))
                resolution = int(input('Разрешение: '))
                Storage.store_area.append(str(Scanner(model, paper_size, manufacturer, price, resolution)))
                if Storage.overall.get(type_eq) is not None:
                    Storage.overall[type_eq] += 1
                else:
                    Storage.overall.setdefault(type_eq, 1)
            elif type_eq == 'Копир':
                model = str(input('Модель: '))
                paper_size = str(input('Размер бумаги: '))
                manufacturer = str(input('Производитель: '))
                price = float(input('Цена: '))
                copy_speed = str(input('Скорость копирования: '))
                Storage.store_area.append(str(Copier(model, paper_size, manufacturer, price, copy_speed)))
                if Storage.overall.get(type_eq) is not None:
                    Storage.overall[type_eq] += 1
                else:
                    Storage.overall.setdefault(type_eq, 1)
        except ValueError:
            print('Недопустимое значение!')
        except ErrorView as error:
            print(error)


class ErrorView(Exception):
    def __init__(self, txt):
        self.txt = txt


class Printer(Equipment):
    def __init__(self, model, paper_size, manufacturer, price, print_type, print_speed):
        super().__init__('Принтер', model, paper_size, manufacturer, price)
        self.print_type = print_type
        self.print_speed = print_speed

    def __str__(self):
        return f'Принтер: модель - {self.model}, формат бумаги -  {self.paper_size},' \
               f' производитель - {self.manufacturer}, цена - {self.price} руб.,' \
               f' тип печати - {self.print_type}, скорость печати - {self.print_speed} л/мин'


class Scanner(Equipment):
    def __init__(self, model, paper_size, manufacturer, price, resolution):
        super().__init__('Сканер', model, paper_size, manufacturer, price)
        self.resolution = resolution

    def __str__(self):
        return f'Сканер: модель - {self.model}, формат бумаги -  {self.paper_size},' \
               f' производитель - {self.manufacturer}, цена - {self.price} руб.,' \
               f' разрешение - {self.resolution}'


class Copier(Equipment):
    def __init__(self, model, paper_size, manufacturer, price, copy_speed):
        super().__init__('Копир', model, paper_size, manufacturer, price)
        self.copy_speed = copy_speed

    def __str__(self):
        return f'Копир: модель - {self.model}, формат бумаги -  {self.paper_size},' \
               f' производитель - {self.manufacturer}, цена - {self.price} руб.,' \
               f' скорость копирования - {self.copy_speed}'


Equipment.entrance()
Equipment.control()
