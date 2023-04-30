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


class TechStore:
    store_dict = {}

    @staticmethod
    def reception(new_tech):
        print(f"Добавляем на склад {new_tech} укажите количество :", end='')
        try:
            quantity = int(input())
            el_q = 0
            for el in TechStore.store_dict.keys():
                if el == new_tech:
                    el_q = TechStore.store_dict.get(new_tech)
            TechStore.store_dict.update({new_tech: quantity + el_q})
        except ValueError:
            print("Необходимо вводить целые числа!!")

    @staticmethod
    def transfer(store_tech, quantity, company_name):
        print(f"Пытаемся переместить в: '{company_name}' {store_tech} в количестве {quantity} штук")
        el_q = 0
        for el in TechStore.store_dict.keys():
            if el == store_tech:
                el_q = TechStore.store_dict.get(store_tech)
        if el_q > quantity:
            TechStore.store_dict.update({store_tech: el_q - quantity})
            print(f"Успешно переместили в компанию {company_name} {store_tech}, "
                  f"{quantity} штук, остаток на складе {el_q - quantity} штук")
        else:
            print(f"Такого количества: {quantity} техники:{store_tech} нет на складе, остаток {el_q} штук")

    @staticmethod
    def store_state():
        print("Состояние склада:")
        for el in TechStore.store_dict:
            print(f"{el}, количество: {TechStore.store_dict[el]}")


class Technic:
    def __init__(self, tech_type, manufacturer, model, price):
        self.tech_type = tech_type
        self.manufacturer = manufacturer
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.tech_type}, {self.manufacturer} {self.model}"


class Printer(Technic):
    def __init__(self, manufacturer, model, price, colour_capable, max_resolution):
        Technic.tech_type = 'Принтер'
        super().__init__(Technic.tech_type, manufacturer, model, price)
        self.colour_capable = colour_capable
        self.max_resolution = max_resolution


class Scaner(Technic):
    def __init__(self, manufacturer, model, price, max_resolution, auto_feeder):
        Technic.tech_type = 'Сканер'
        super().__init__(Technic.tech_type, manufacturer, model, price)
        self.max_resolution = max_resolution
        self.auto_feeder = auto_feeder


class Xerox(Technic):
    def __init__(self, manufacturer, model, price, max_resolution, colour_capable, auto_feeder):
        Technic.tech_type = 'Ксерокс'
        super().__init__(Technic.tech_type, manufacturer, model, price)
        self.max_resolution = max_resolution
        self.colour_capable = colour_capable
        self.auto_feeder = auto_feeder


printer1 = Printer('Epson', '3170', 2000, 'BW', '4800x4800')
printer2 = Printer('Canon', '2170', 2000, 'BW', '4800x4800')
scaner1 = Scaner('Canon', 'EasyScan', 2000, '4800x4800', 'auto_feeder')
xerox1 = Xerox('XEROX', 'WorkCentre 2500', 2000, '2400x4800', 'BW', 'auto_feeder')
my_store = TechStore()
my_store.reception(printer1)
my_store.reception(printer1)
my_store.reception(printer1)
my_store.reception(printer2)
my_store.reception(scaner1)
my_store.transfer(printer1, 20, 'ДНС')
my_store.transfer(printer1, 330, 'Ситилинк')
my_store.transfer(printer2, 30, 'ДНС')
my_store.transfer(scaner1, 30, 'ДНС')
my_store.transfer(xerox1, 20, 'Фотосклад')
my_store.store_state()
