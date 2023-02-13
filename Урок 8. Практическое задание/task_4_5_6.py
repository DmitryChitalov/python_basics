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
class OfficeEquipment:
    def __init__(self, name, price, quantity, number_of_lists):
        self.name = name
        self.price = price
        self.numb = number_of_lists
        try:
            if isinstance(quantity, int):
                self.quantity = quantity
                self.my_unit = {
                    'Модель устройства': self.name,
                    'Цена за устройство': self.price,
                    'Количество устройств': self.quantity}
            else:
                self.my_unit = {}
                raise MyOwnExc("Вы ввели не число, данные не будут добавлены в словарь")
        except MyOwnExc as e:
            print(e.txt)
class Warehouse:
    goods = []
    @classmethod
    def reception(cls, obj):
        cls.goods.append(obj.my_unit)
    @classmethod
    def put_to_div(cls, obj, div):
        pass
class Printer(OfficeEquipment):
    def to_print(self):
        return f'to print smth {self.numb} times'
class Scanner(OfficeEquipment):
    def to_scan(self):
        return f'to scan smth {self.numb} times'
class Copier(OfficeEquipment):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'
unit_1 = Printer('hp', 4000, 5, 10)
unit_2 = Scanner('Canon', 3000, 5, 10)
Warehouse.reception(unit_1)
Warehouse.reception(unit_2)
print(Warehouse.goods)
print(unit_2.to_scan())
print(unit_1.to_print())
