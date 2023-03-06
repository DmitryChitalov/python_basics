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

# pylint: disable=missing-class-docstring, attribute-defined-outside-init, f-string-without-interpolation,bare-except,missing-function-docstring


class Warehouse():
    def __init__(self, name, cost, weight):
        self.name = name
        self.cost = cost
        self.weight = weight
        self.reception = []
        self.org_propreties = {
            "Наименование": name, "Цена": cost, "Вес": weight}

    def recep(self):
        try:
            org_a = int(input(f'Введите цену за ед: '))
            org_b = int(input(f'Введите вес: '))
            org_с = input(f'Введите наименование: ')
            org_tech = {'Наименование': org_с, 'Цена': org_a, 'Вес': org_b}
            self.org_propreties.update(org_tech)
            self.reception.append(self.org_propreties)
            print(f'Текущий список -\n {self.reception}')
        except:
            return f'Ошибка ввода данных'


class Printer(Warehouse):
    def speeds(self, speed):
        self.speed = speed
        return self.name, self.cost, self.weight, self.speed


class Scanner(Warehouse):
    def colours(self, colour):
        self.colour = colour
        return self.name, self.cost, self.weight, self.colour


class Copier(Warehouse):
    def copies(self, mcopies):
        self.mcopies = mcopies
        return self.name, self.cost, self.weight, self.mcopies


a = Copier("Canon", 8000, 9)
print(a.copies(10))

b = Scanner("Xerox", 4000, 2)
print(b.colours(7))

c = Printer("HP", 4000, 2)
print(c.speeds(4096))
