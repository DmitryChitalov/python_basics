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


class Warehouse():
    movement = []
    movement_str = {"technic": "", "quantity": 0, "direction": ""}
    name = ""
    face = ""

    def __init__(self, name, face):
        self.name = name
        self.face = face

    def move(self, technik, quantity, direction):
        self.movement_str = {"technic": technik, "quantity": quantity,
                             "direction": direction}
        if self.movement_str != None:
            self.movement.append(self.movement_str)

    def __setattr__(self, key, value):
        if key == 'movement_str':
            try:
                tmp = value["technic"].inv_number
                tmp = int(value["quantity"])
            except:
                object.__setattr__(self, key, None)
                print("Недопустимое имя атрибута")
            else:
                object.__setattr__(self, key, value)
        else:
            object.__setattr__(self, key, value)


class technic():
    inv_number = 0
    firm = ""
    prefix_inv_number = ""


class scaner(technic):
    prefix_inv_number = "sc"
    permission = 600


class printer(technic):
    prefix_inv_number = "pr"
    cartridge = ""
    pass


class xerox(technic):
    prefix_inv_number = "x"
    net = bool
    pass


my_wh = Warehouse("Мой склад", "Иванов")
technic = scaner()
technic.inv_number = 1
technic.firm = "Firm Scanner"
my_wh.move(technic, 3, "dir 1")
my_wh.move(technic, -1, "dir 2")

technic = printer()
technic.inv_number = 2
technic.cartridge = "old"
my_wh.move(technic, 5, "dir 1")
# проверяем не добавляем
my_wh.move("technic", 5, "dir 1")
# проверяем не добавляем
my_wh.move(technic, "ds", "dir 1")

print(my_wh)
print()
print(my_wh.movement)
