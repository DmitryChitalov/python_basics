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


class store:
    store_dict = {}

    def reception(self, technic):
        print(f"Добавляем на склад {technic} укажите количество :", end='')
        try:
            quantity = int(input())
            el_q = 0
            for el in self.store_dict.keys():
                if el == technic:
                    el_q = self.store_dict.get(technic)
            self.store_dict.update({technic: quantity + el_q})
        except ValueError:
            print("Необходимо вводить целые числа!!")

    def transfer(self, technic, quantity, company_name):
        self.quantity = quantity
        self.company_name = company_name
        print(f"Пытаемся переместить в: '{company_name}' {technic} в количестве {quantity} штук")
        el_q = 0
        for el in self.store_dict.keys():
            if el == technic:
                el_q = self.store_dict.get(technic)
        if el_q > quantity:
            self.store_dict.update({technic: el_q - quantity})
            print(f"Отправляем в компанию {company_name} {technic}, "
                  f"{self.quantity} штук")
        else:
            print(f"Такого количества: {quantity} техники:{technic} нет на складе")

    def store_state(self):
        print("Состояние склада:")

        for el in self.store_dict:
            print(f"{el}, количество: {self.store_dict[el]}")


class technic:
    def __init__(self, tech_type, manufacturer, model, price):
        self.tech_type = tech_type
        self.manufacturer = manufacturer
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.tech_type}, {self.manufacturer} {self.model}"


class printer(technic):
    def __init__(self, manufacturer, model, price, colour_capable, max_resolution):
        technic.tech_type = 'Принтер'
        super().__init__(technic.tech_type, manufacturer, model, price)
        self.colour_capable = colour_capable
        self.max_resolution = max_resolution


class scaner(technic):
    def __init__(self, manufacturer, model, price, max_resolution, auto_feeder):
        technic.tech_type = 'Сканер'
        super().__init__(technic.tech_type, manufacturer, model, price)
        self.max_resolution = max_resolution
        self.auto_feeder = auto_feeder


class xerox(technic):
    def __init__(self, manufacturer, model, price, max_resolution, colour_capable, auto_feeder):
        technic.tech_type = 'Ксерокс'
        super().__init__(technic.tech_type, manufacturer, model, price)
        self.max_resolution = max_resolution
        self.colour_capable = colour_capable
        self.auto_feeder = auto_feeder


printer1 = printer('Epson', '3170', 2000, 'BW', '4800x4800')
printer2 = printer('Canon', '2170', 2000, 'BW', '4800x4800')
scaner1 = scaner('Canon', 'EasyScan', 2000, '4800x4800', 'auto_feeder')
xerox1 = xerox('XEROX', 'WorkCentre 2500', 2000, '2400x4800', 'BW', 'auto_feeder')
my_store = store()
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
