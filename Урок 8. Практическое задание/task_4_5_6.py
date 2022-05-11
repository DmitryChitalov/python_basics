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
                    'Цена за ед': self.price,
                    'Количество': self.quantity}
            else:
                self.my_unit = {}
                raise MyOwnExc("Вы ввели не число, словарь будем пустым")

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


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
Warehouse.reception(unit_1)
Warehouse.reception(unit_2)

print(Warehouse.goods)

print(unit_2.to_scan())
