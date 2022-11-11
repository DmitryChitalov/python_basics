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


class MyOwnExc(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    units = []

    @classmethod
    def recieve(cls, obj):
        cls.units.append(obj.unit)


class OfficeDevices:
    def __init__(self, id, model_name, price):
        self.id = id
        self.model_name = model_name
        self.price = price
        try:
            if isinstance(price, int):
                self.price = price
                self.unit = {
                    'Device ID': self.id,
                    'Model': self.model_name,
                    'Price': self.price}
            else:
                raise MyOwnExc("Ошибка в вводе данных - цена должна быть числом")
        except MyOwnExc as e:
            print(e.txt)

    def set_id_model(self):
        id = input('введите айди')
        model = input('введите модель')


class Printer(OfficeDevices):

    def __init__(self, number_of_colours, *args):
        super().__init__(*args)
        self.nuber_of_colours = number_of_colours

    def set_colours(self):
        colours = input('введите кол-во цветов')


class Scaner(OfficeDevices):
    def __init__(self, dpi, *args):
        super().__init__(*args)
        self.dpi = dpi


class Xerox(OfficeDevices):
    def __init__(self, weight, *args):
        super().__init__(*args)
        self.weight = weight


obj1 = Printer(2, '334121EE', "Xerox6020", 8500)
Warehouse.recieve(obj1)
obj2 = Scaner(800, 'D3432dfs', "SuperScaner2000", 3000)
Warehouse.recieve(obj2)
obj3 = Xerox("50kg", 'D23a', "ExpensivePrint3000", 99999)
Warehouse.recieve(obj3)
print(Warehouse.units)