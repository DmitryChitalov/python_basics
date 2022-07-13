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


class OfficeEquipment:
    """info"""

    def __init__(self, name, price, quantity, number_of_lists):
        self.name = name
        self.price = price
        self.numb = number_of_lists
        try:
            if isinstance(quantity, int):
                self.quantity = quantity
                self.my_unit = {
                    'Модель устройства': self.name,
                    'Цена за ед': self.price,
                    'Количество': self.quantity}
            else:
                self.my_unit = {}
                raise MyOwnExc("Вы ввели не число, словарь будем пустым")

        except MyOwnExc as doc:
            print(doc.txt)


class MyOwnExc(Exception):
    """info"""
    def __init__(self, txt):
        super(__class__, self).__init__()
        self.txt = txt


class Warehouse:
    """info"""
    goods = []

    @classmethod
    def reception(cls, obj):
        """info"""
        cls.goods.append(obj.my_unit)

    @classmethod
    def put_to_div(cls, obj, div):
        """info"""


class Printer(OfficeEquipment):
    """info"""

    def to_print(self):
        """info"""
        return f'to print smth {self.numb} times'


class Scanner(OfficeEquipment):
    """info"""

    def to_scan(self):
        """info"""
        return f'to scan smth {self.numb} times'


class Copier(OfficeEquipment):
    """info"""

    def to_copier(self):
        """info"""
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('hp', 30000, 2, 10)
unit_2 = Scanner('Canon', 18000, 1, 10)
Warehouse.reception(unit_1)
Warehouse.reception(unit_2)

print(Warehouse.goods)
print(unit_2.to_scan())
