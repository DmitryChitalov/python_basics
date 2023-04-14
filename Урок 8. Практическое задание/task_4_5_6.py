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
import pprint

class OfficeEquipment:
    def __init__(self, name, price, quantity, number_of_lists):
        self.name = name
        self.price = price
        self.number_of_lists = number_of_lists

        try:
            if isinstance(quantity, int):

                self.quantity = quantity

                self.warehouse_units = {
                    "Модель устройства": self.name,
                    "Цена за ед": self.price,
                    "Количество": self.quantity}
            else:
                self.warehouse_units = {}
                raise CustomExceptionError("На ввод принимаются только числа.")

        except CustomExceptionError as custom_error:
            print(custom_error.txt)


class CustomExceptionError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Printer(OfficeEquipment):
    def please_print_me(self):
        return f"Печатать можно {self.number_of_lists} раз."


class Scanner(OfficeEquipment):
    def please_scan_me(self):
        return f"Сканировать можно {self.number_of_lists} раз."


class Copier(OfficeEquipment):
    def please_copy_me(self):
        return f"Копировать можно {self.number_of_lists} раз."

class Warehouse:
    goods = []

    @classmethod
    def reception(cls, obj):
        cls.goods.append(obj.warehouse_units)

first_unit = Printer('Hewlett-Packard', 5000, 8, 12)
Warehouse.reception(first_unit)
second_unit = Scanner('Canon', 4111, 12, 6)
Warehouse.reception(second_unit)
third_unit = Scanner('Ricoh', 2088, 18, 7)
Warehouse.reception(third_unit)

# whole_sale = Warehouse()
# whole_sale()

for i in Warehouse.goods:
    pprint.pprint(i)
