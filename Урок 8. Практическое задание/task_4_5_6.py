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

6. Продолжить работу над пятым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


class OEStorage:

    def __init__(self, address, capacity, org_structure):  # адрес, вместимость склада, орг. структура компании
        self.address = address
        self.capacity = capacity
        self.org_structure = org_structure
        self.cur_capacity = capacity
        self.storage = dict()

    # формирование списка наименований позиций склада
    def list_update(self, in_obj_name):
        tmp_dict = {in_obj_name: 0}
        self.storage.update(tmp_dict)

    # метод приемки оборудования на склад. реализована доп. проверка остаточной вместимости склада (в кг)
    def acceptance(self, in_obj_name, in_obj_weight, quantity):
        err_text = f"Емкость склада превышена на {quantity * in_obj_weight - self.cur_capacity}!"
        try:
            if quantity * in_obj_weight > self.cur_capacity:
                raise MyException(err_text)
        except MyException as err:
            print(err)
            new_dict = {in_obj_name: self.storage.get(in_obj_name) + self.cur_capacity // in_obj_weight}
            self.storage.update(new_dict)
            self.cur_capacity -= (self.cur_capacity // in_obj_weight) * in_obj_weight
        else:
            new_dict = {in_obj_name: self.storage.get(in_obj_name) + quantity}
            self.storage.update(new_dict)
            self.cur_capacity -= in_obj_weight * quantity
        print(f"Текущее наполнение склада: {self.storage}")
        print(f"Остаточная емкость склада: {self.cur_capacity} кг")

    # метод отгрузки орг. техники в подразделения. реализована проверка наличия необходимого количества на складе
    def dispatch(self, in_obj_name, in_obj_weight, quantity, struct_name):
        err_txt = f"Количество техники на складе - только {self.storage.get(in_obj_name)}!"
        try:
            if quantity > self.storage.get(in_obj_name):
                raise MyException(err_txt)
        except MyException as err:
            print(err)
            print(f"Отгружено в {struct_name} только {self.storage.get(in_obj_name)} единиц техники")
            new_dict = {in_obj_name: 0}
            self.cur_capacity += self.storage.get(in_obj_name) * in_obj_weight
            self.storage.update(new_dict)
        else:
            print(f"Отгружено в {struct_name} {quantity} единиц техники")
            new_dict = {in_obj_name: self.storage.get(in_obj_name) - quantity}
            self.storage.update(new_dict)
            self.cur_capacity += in_obj_weight * quantity
        print(f"Текущее наполнение склада: {self.storage}")
        print(f"Остаточная емкость склада: {self.cur_capacity} кг")

    @staticmethod
    def qty_check(num):
        try:
            if not num.isdigit():
                raise MyException("Введено не число, в операции отказано.")
        except MyException as err:
            print(err)
            return False
        else:
            return True


class OfficeEquipment:

    def __init__(self, name, oe_type, weight):
        self.name = name  # наименование товара
        self.oe_type = oe_type  # тип техники
        self.weight = weight  # вес техники


class Printer(OfficeEquipment):

    def __init__(self, name, weight, color, p_type):
        super().__init__(name, "Printer", weight)
        self.color = color  # признак наличия цветной печати (цветной, ч/б)
        self.p_type = p_type  # тип принтера (лазерный, струйный, матричный)


class Scanner(OfficeEquipment):

    def __init__(self, name, weight, resolution):
        super().__init__(name, "Scanner", weight)
        self.resolution = resolution  # разрешение сканирования


class Copier(OfficeEquipment):

    def __init__(self, name, weight, pages_per_minute):
        super().__init__(name, "Copier", weight)
        self.ppm = pages_per_minute  # производительность копира - страниц в минуту


structure = ["Отдел продаж", "Бухгалтерия", "Финансовый отдел"]  # организационная структура компании
oes_obj = OEStorage("Морская наб., 1", 100, structure)  # инициализация склада
pr_obj1 = Printer("Canon Ultra", 7, "color", "laser")
pr_obj2 = Printer("HP X1", 4, "black", "matrix")
sc_obj = Scanner("Canon Pixma", 2, 400)
cp_obj = Copier("Xerox 1235", 5, 37)

'''
print(oes_obj.__dict__)
print(pr_obj1.__dict__)
print(pr_obj2.__dict__)
print(sc_obj.__dict__)
print(cp_obj.__dict__)
'''

# инициализация перечня товаров, доступных для приемки и отгрузки
oes_obj.list_update(pr_obj1.name)
oes_obj.list_update(pr_obj2.name)
oes_obj.list_update(sc_obj.name)
oes_obj.list_update(cp_obj.name)

# приемка оборудования на склад
oes_obj.acceptance(pr_obj1.name, pr_obj1.weight, 10)
in_qty = input("Введите количество принимаемого товара (принтер типа 2):")
if OEStorage.qty_check(in_qty):
    oes_obj.acceptance(pr_obj2.name, pr_obj2.weight, int(in_qty))
oes_obj.acceptance(sc_obj.name, sc_obj.weight, 1)
oes_obj.acceptance(cp_obj.name, cp_obj.weight, 1)
print()

# отгрузка оборудования в подразделения
oes_obj.dispatch(pr_obj1.name, pr_obj1.weight, 12, structure[1])
in_qty = input("Введите количество отгружаемого товара (принтер типа 2):")
if OEStorage.qty_check(in_qty):
    oes_obj.dispatch(pr_obj2.name, pr_obj2.weight, int(in_qty), structure[2])
