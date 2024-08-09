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

# 4-е Задание:
# Создал Родительский класс class Storage() и класс-наследник StorageOfficeEquipment с дополнительными уникальными параметрами.
# Также создал родительский класс OfficeEquipment() и классы-наследники Printer(OfficeEquipment),
# Scaner(OfficeEquipment) и Xerox(OfficeEquipment) со своими уникальными параметрами.

# 5-е Задание:
# Внутри класса StorageOfficeEquipment(Storage) создал два метода:
# 1) acceptance2(self, equipment_name, quantit) - отвечает за приём оборудования на склад.
# 2) distribution(self, equipment_name, quantit, unit) - отвечает за распределение оборудования по подразделениям.

# 6-е Задание:
# Внутри метода acceptance2(self, equipment_name, quantit) реализовал валидацию на название оборудования.
# Если введено не корректное название, то программа оповестит об этом.
# Внутри метода distribution(self, equipment_name, quantit, unit) реализовал валидацию на название подразделение и название оборудования.
# Если введены неправильно название подразделения или оборудования, то программа оповестит об этом.


#Родительский класс Storage
class Storage():
    #Атрибуты экземпляра - название и площадь в квадратных метрах
    def __init__(self, name, square_meters):
        self.square_meters = square_meters
        self.name = name


#Класс-наследник StorageOfficeEquipment(Storage)
class StorageOfficeEquipment(Storage):

    # Атрибуты класса - printer, scaner, xerox.
    # Эти переменные хранят данные о наличии оборудования на складе и в 3-х подразделениях.
    printer = {"склад": 0, "отдел продаж": 0, "отдел обслуживания": 0, "отдел рекламы": 0}
    scaner = {"склад": 0, "отдел продаж": 0, "отдел обслуживания": 0, "отдел рекламы": 0}
    xerox = {"склад": 0, "отдел продаж": 0, "отдел обслуживания": 0, "отдел рекламы": 0}

    # Атрибуты экземпляра - название склада, площадь в квадратных метрах (родительские параметры) и температура помещения (уникальный параметр)
    def __init__(self, name, squre_meters, temperature):
        super().__init__(name, squre_meters)
        self.temperature = temperature

    # Cледующая функция accacceptance2() принимает
    # одно из трёх названий оборудования - "принтер", "cканер", "ксерокс".
    # И сохраняет эти данные в виде кортеджа. Например, ('На складе в наличии:', {'ксерокс': 10}).
    def acceptance2(self, equipment_name, quantit):
        if equipment_name == "принтер":
            StorageOfficeEquipment.printer["склад"] += quantit
            return "На складе в наличии:", {equipment_name: StorageOfficeEquipment.printer["склад"]}

        elif equipment_name == "сканер":
            StorageOfficeEquipment.scaner["склад"] += quantit
            return "На складе в наличии:", {equipment_name: StorageOfficeEquipment.scaner["склад"]}

        elif equipment_name == "ксерокс":
            StorageOfficeEquipment.xerox["склад"] += quantit
            return "На складе в наличии:", {equipment_name: StorageOfficeEquipment.xerox["склад"]}
        else:
            return f'''Вы ввели некорректное название оборудование.
            Функция acceptance2 принимает одно из трёх названий - "принтер", "cканер", "ксерокс", - и количество .
            Пожалуйста, введите корректные данные.
            '''

    # Cледующая функция distribution принимает:
    # 1) одно из трёх названий оборудования - "принтер", "cканер", "ксерокс";
    # 2) количество оборудования, которое запрашивается со склада;
    # 3) название подразделения - "отдел продаж" или "отдел обслуживания" или "отдел рекламы", - которое запрашивает оборудование.
    # Далее функция передаёт со склада указанное оборудование в указанное подразделение, обнавляет данные в словарях -
    # printer, scaner, xerox, - и возвразщает свежие данные о наличии указанного оборудования в виде кортеджа.
    # Например, ('Всего принтеров в наличии', {'склад': 10, 'отдел продаж': 4, 'отдел обслуживания': 2, 'отдел рекламы': 4})
    def distribution(self, equipment_name, quantit, unit):

        if unit == "отдел продаж" or unit == "отдел обслуживания" or unit == "отдел рекламы":
            if equipment_name == "принтер":
                StorageOfficeEquipment.printer["склад"] -= quantit
                StorageOfficeEquipment.printer[unit] += quantit
                return "Всего принтеров в наличии", StorageOfficeEquipment.printer

            elif equipment_name == "сканер":
                StorageOfficeEquipment.scaner["склад"] -= quantit
                StorageOfficeEquipment.scaner[unit] += quantit
                return "Всего сканеров в наличии", StorageOfficeEquipment.scaner

            elif equipment_name == "ксерокс":
                StorageOfficeEquipment.xerox["склад"] -= quantit
                StorageOfficeEquipment.xerox[unit] += quantit
                return "Всего ксероксов в наличии", StorageOfficeEquipment.xerox

            else:
                return '''
        Вы ввели некорректное название оборудование.
        Функция distribution принимает:
        1) одно из трёх названий оборудования - "принтер", "cканер", "ксерокс";
        2) количество оборудования, которое запрашивается со склада;
        3) название подразделения - "отдел продаж" или "отдел обслуживания" или "отдел рекламы", - которое запрашивает оборудование.                   
                
            Пожалуйста, введите корректные данные.'''

        else:
            return '''
        Вы ввели некорректное название подразделения.
        Функция distribution принимает:
        1) одно из трёх названий оборудования - "принтер", "cканер", "ксерокс";
        2) количество оборудования, которое запрашивается со склада;
        3) название подразделения - "отдел продаж" или "отдел обслуживания" или "отдел рекламы", - которое запрашивает оборудование.                   
                
        Пожалуйста, введите корректные данные.
        '''

#Родительский класс OfficeEquipment
class OfficeEquipment():
    def __init__(self, name, color):
        self.name = name
        self.color = color


#Класс-наследник Printer(OfficeEquipment)
class Printer(OfficeEquipment):
    # Атрибуты экземпляра класса - название и цвет (родительские параметры) и скорость печати одного листа (уникальный параметр)
    def __init__(self, name, color, print_speed):
        super().__init__(name, color)
        self.print_speed = prind_speed


#Класс-наследник Scaner(OfficeEquipment)
class Scaner(OfficeEquipment):
    # Атрибуты экземпляра класса - название и цвет (родительские параметры) и скорость сканирования одного листа (уникальный параметр)
    def __init__(self, name, color, scan_speed):
        super().__init__(name, color)
        self.scan_speed = scan_speed

#Класс-наследник Xerox(OfficeEquipment)
class Xerox(OfficeEquipment):
    # Атрибуты экземпляра класса - название и цвет (родительские параметры) и максимально-допустисый формат листа (уникальный параметр)
    def __init__(self, name, color, sheet_format):
        super().__init__(name, color)
        self.sheet_format = sheet_format

#Проверка работы классов и их методов
xerox_i28 = Xerox("Kodak", "black", "A1")
print(xerox_i28.name, xerox_i28.color, xerox_i28.sheet_format)

mobius_storage = StorageOfficeEquipment("Мобиус1", 200, 22)
print(mobius_storage.name, mobius_storage.square_meters, mobius_storage.temperature)
print(mobius_storage.acceptance2("принтер", 20))
print(mobius_storage.acceptance2("сканер", 40))
print(mobius_storage.acceptance2("ксерокс", 10))
print(mobius_storage.distribution("принтер", 4, "отдел рекламы"))
print(mobius_storage.distribution("принтер", 4, "отдел продаж"))
print(mobius_storage.distribution("принтер", 2, "отдел обслуживания"))
print(mobius_storage.distribution("сканер", 3, "отдел рекламы"))
print(mobius_storage.distribution("ксерокссссс", 1, "отдел рекламы"))







