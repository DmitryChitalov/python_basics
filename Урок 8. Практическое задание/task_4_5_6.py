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
class NoEmptyCellsError(Exception):
    """ Класс исключений при недостаточном количестве свободных ячеек на складе """

    def __init__(self, txt):
        self.txt = txt


class TooWeightError(Exception):
    """ Класс исключений при большой массе техники на 1 занимаемую ячейку """

    def __init__(self, txt):
        self.txt = txt


class NotEnoughQuantityError(Exception):
    """ Класс исключений при недостаточном количестве техники на складе """

    def __init__(self, txt):
        self.txt = txt


class Storage:
    """ Класс для описания склада """

    def __init__(self, cells, weight_per_cell):
        self.cells = cells  # всего ячеек на складе
        self.empty_cells = cells  # количество свободных ячеек в текущий момент
        self.weight_per_cell = weight_per_cell  # наибольшая допустимая нагрузка на одну ячейку
        self.on_storage = {}  # словарь хранимой техники формата модель: количество

    @property
    def get_empty_cells(self):
        """ Возвращает количество свободных ячеек """
        return f'Осталось {self.empty_cells} свободных ячеек'

    def to_storage(self, office_equipment, quantity=1):
        """ Принимает технику на хранение и выводит количество свободных ячеек"""
        try:  # обработка исключения, когда количество не является числом
            quantity = int(quantity)
        except ValueError:
            print("Количество должно быть числом")
        else:
            try:  # обработка исключения, когда недостаточно свободных ячеек
                if self.empty_cells < office_equipment.volume * quantity:
                    raise NoEmptyCellsError("Недостаточно свободных ячеек для данного размера техники")
            except NoEmptyCellsError as e:
                print(e)
            else:
                try:  # обработка исключения, когда превышается допустимая нагрузка на ячейку
                    if office_equipment.weight / office_equipment.volume > self.weight_per_cell:
                        raise TooWeightError("Техника слишком тяжелая для данного склада")
                except TooWeightError as e:
                    print(e)
                else:
                    # получение текущего количества данной техники на складе, при отсутствии создание пары модель: None
                    numbers = self.on_storage.setdefault(office_equipment.model)
                    if numbers:
                        self.on_storage[office_equipment.model] += quantity
                    else:
                        self.on_storage[office_equipment.model] = quantity
                    self.empty_cells -= office_equipment.volume * quantity  # уменьшение кол-ва свободных ячеек
                    print(f"Техника {office_equipment} в количестве {quantity} помещена на склад")
                    print(self.get_empty_cells)

    def from_storage(self, office_equipment, department, quantity=1):
        try:
            quantity = int(quantity)
        except ValueError:
            print("Количество должно быть числом")
        else:
            try:  # Обработка исключения при недостаточном количестве техники на складе
                if self.on_storage[office_equipment.model] < quantity:
                    raise NotEnoughQuantityError(f"Недостаточно товара {office_equipment.model} на складе")
            except NotEnoughQuantityError as e:
                print(e)
            else:
                self.on_storage[office_equipment.model] -= quantity
                self.empty_cells += quantity * office_equipment.volume  # увеличение кол-ва свободных ячеек
                print(f"Техника {office_equipment} в количестве {quantity} помещена в {department}")
                print(self.get_empty_cells)


class OfficeEquipment:
    def __init__(self, brand, model, price, weight, volume):
        self.brand = brand
        self.model = model
        self.price = price
        self.weight = weight  # масса техники
        self.volume = volume  # количество занимаемых ячеек

    def __str__(self):
        return f'{self.brand} {self.model}'


class Printer(OfficeEquipment):
    def __init__(self, brand, model, price, weight, volume, type):
        super().__init__(brand, model, price, weight, volume)
        self.type = type  # тип принтера


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, price, weight, volume, resolution):
        super().__init__(brand, model, price, weight, volume)
        self.resolution = resolution  # разрешение сканера


class Copier(OfficeEquipment):
    def __init__(self, brand, model, price, weight, volume, is_colour):
        super().__init__(brand, model, price, weight, volume)
        self.is_colour = is_colour  # цветной или нет


# проверка реализации
print_1 = Printer('HP', "model1", 3000, 15, 2, 'струйный')
scan_1 = Scanner('Epson', "model2", 4000, 10, 1, 1200)
scan_2 = Scanner('Epson', "model3", 5000, 10, 2, 1200)
copier_1 = Copier('Xerox', "xe1", 1000, 25, 3, True)
storage1 = Storage(30, 9.99)

print(storage1.get_empty_cells)
storage1.to_storage(print_1)
storage1.to_storage(copier_1, 3)
storage1.to_storage(copier_1, 100)
storage1.to_storage(copier_1, 'один')
storage1.to_storage(scan_1)
storage1.to_storage(scan_2)
storage1.to_storage(scan_2)

storage1.from_storage(copier_1, 'бухгалтерия')
storage1.from_storage(copier_1, 'бухгалтерия', 3)
storage1.from_storage(scan_2, 'бухгалтерия', 'два')
