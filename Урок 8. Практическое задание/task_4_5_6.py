"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс,
описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа
оргтехники.

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

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = {'Model is ': self.name, 'Price for one is ': self.price,
                      'Amount is ': self.quantity}

    def income(self):
        try:
            name = input(f'Enter model name: ')
            price = int(input(f'Enter price for one: '))
            quantity = int(input(f'Enter amount: '))
            item = {'Model is ': name, 'Prise for one is ': price,
                    'Amount is ': quantity}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print('Wrong name')


class Printer(OfficeEquipment):
    pass


class Scanner(OfficeEquipment):
    pass


class Xerox(OfficeEquipment):
    pass


p = Printer('Model of Printer', 2, 300)
s = Scanner('Model of Scanner', 54000, 10)
x = Xerox('Model of Xerox', 7000, 15)
p.income()
s.income()
x.income()
