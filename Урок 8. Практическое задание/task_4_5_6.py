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
#Task_4_5_6
class Warehouse:
    def __init__(self) -> None:
        self.warehouse_list = []

    def receipt(self, equipment):
        self.warehouse_list.append(equipment)


class Officequipment:
    def __init__(self,
                 type_equipmen,
                 prod_name,
                 qty,
                 unit) -> None:
        self.type_equipmen = type_equipmen
        self.prod_name = prod_name
        self.qty = qty
        self.unit = unit


class Printer(Officequipment):
    def __init__(self,
                 type_equipmen,
                 prod_name,
                 qty,
                 unit,
                 print_type) -> None:
        self.print_type = print_type
        super().__init__(type_equipmen, prod_name, qty, unit)


class Scaner(Officequipment):
    def __init__(self,
                 type_equipmen,
                 prod_name,
                 qty,
                 unit,
                 scan_type) -> None:
        self.scan_type = scan_type
        super().__init__(type_equipmen, prod_name, qty, unit)


class Copier(Officequipment):
    def __init__(self,
                 type_equipmen,
                 prod_name,
                 qty,
                 unit,
                 copy_pm) -> None:
        self.copy_pm = copy_pm
        super().__init__(type_equipmen, prod_name, qty, unit)


class MyExceptionQty(Exception):
    def __init__(self, qty):
        self.qty = qty

    def __str__(self):
        return f"Недопустимое значение {self.qty}"


wh = Warehouse()
ex = "y"
while ex != "n":
    prod_inp = {}
    prod_type = input('Введите тип товара(1 - принтер, 2 - сканер, 3 - копир): ')
    if prod_type == '1':
        prod_inp['Тип'] = 'принтер'
    elif prod_type == '2':
        prod_inp['Тип'] = 'сканер'
    else:
        prod_inp['Тип'] = list('копир')

    prod_inp['Наименование'] = input('Введите название товара: ')

    control = True
    while control:
        num = input('Введите количество товара: ')
        try:
            if not num.isdigit():
                raise MyExceptionQty(num)
        except MyExceptionQty as e:
            print(e)
        else:
            try:
                if int(num) <= 0:
                    raise MyExceptionQty(num)
            except MyExceptionQty as e:
                print(e)
            else:
                control = False
                prod_inp['количество'] = num
    prod_inp['ед'] = input('Введите ед. измерения товара: ')
    wh.receipt(prod_inp)
    ex = input('Добавить ещё товар?(y/n) ')
print(wh.warehouse_list)
