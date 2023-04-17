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
class Store:
    example = {}

    def get_app(self, equip):
        if not isinstance(equip, Equipment):
            raise Exception('Внимание!')
        if self.example.get(equip) is not None:
            self.example[equip] += 1
        else:
            self.example[equip] = 1

    def result_dict(self):
        for k, v in self.example.items():
            print(f'{k} : {v} шт')


class Equipment:
    def __init__(self, type_t: str, model: str, cost: float):
        self.type_tech = type_t
        self.model = model
        self.cost = cost
    def __str__(self):
        return f" {self.model}"


class Printer(Equipment):
    def __init__(self,  type_a: str, model: str, cost: float):
        super().__init__('Принтер', model, cost)
        self.type = type_a


class Scanner(Equipment):
    def __init__(self, model: str, cost: float, type_b: str):
        super().__init__('Сканер', model, cost)
        self.type = type_b


class Xerox(Equipment):
    def __init__(self, model: str, cost: float, dpi: str):
        super().__init__('Ксерокс', model, cost)
        self.dpi = dpi


pr_1 = Printer('Лазерный', 'Canon', 1700)
pr_2 = Printer('Светодиодный', 'HP', 1900)

scan_1 = Scanner('Intel', 3500, 'Книжный')
scan_2 = Scanner('Zeno Scan', 10000, 'Планшетный')

xerox_1 = Xerox('Xerox WorkCentre',  3400, '1200 х 2400')
xerox_2 = Xerox('RazerXerox WorkCentre 6015', 5000, '1200 x2400')
store = Store()

store.get_app(pr_1)
store.get_app(pr_2)
store.get_app(scan_1)
store.get_app(scan_2)
store.get_app(xerox_1)
store.get_app(xerox_2)

store.result_dict()
