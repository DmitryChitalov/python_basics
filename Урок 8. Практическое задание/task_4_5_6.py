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


class Warehouse:
    goods = []
    div = []

    def reception(self, obj):
        self.goods.append(obj.my_unit)

    def put_to_div(self, obj, div):
        division = {'Устройство': obj.name, 'Отдел': div}
        self.div.append(division)

    def print_stock(self):
        print(self.goods)


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
                    'Цена за ед': self.price,
                    'Количество': self.quantity}
            else:
                self.my_unit = {}
                raise ValueError("Вы ввели не число, словарь будем пустым")
        except ValueError as e:
            print(e.txt)


class Printer(OfficeEquipment):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(OfficeEquipment):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(OfficeEquipment):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


warehouse = Warehouse()
printer = Printer('hp', 2500, 10, 12)
scanner = Scanner('Canon', 1250, 7, 14)
warehouse.reception(printer)
warehouse.reception(scanner)
warehouse.put_to_div(printer, 'Отдел 1')
warehouse.put_to_div(scanner, 'Отдел 2')

print(warehouse.goods)
print(scanner.to_scan())
print(warehouse.div)
