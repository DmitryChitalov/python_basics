"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы 
— конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите 
параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, 
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за 
приём оргтехники на склад и передачу в определённое подразделение компании. Для 
хранения данных о наименовании и количестве единиц оргтехники, а также других данных, 
можно использовать любую подходящую структуру (например, словарь).
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых 
пользователем данных. Например, для указания количества принтеров, отправленных на 
склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум 
возможностей, изученных на уроках по ООП.

"""
class Storage:
    some_dict = {}

    def receive(self, items):
        if not isinstance(items, Devices):
            raise Exception("Error")
        if self.some_dict.get(items) is not None:
            self.some_dict[items] += 1
        else:
            self.some_dict[items] = 1

    def result_dict(self):
        for a, b in self.some_dict.items():
            print(f"{a} - {b} item(s)")


class Devices:
    def __init__(self, type_tech: str, brand: str, model: str, cost: float):
        self.type_tech = type_tech
        self.brand = brand
        self.model = model
        self.cost = cost

    def __str__(self):
        return f"{self.brand} {self.model}"


class Laptop(Devices):
    def __init__(self, brand: str, model: str, cost: float, type_: str):
        super().__init__("Laptop", brand, model, cost)
        self.type = type_


class Scanner(Devices):
    def __init__(self, brand: str, model: str, cost: float, colors: str):
        super().__init__("Scanner", brand, model, cost)
        self.colors = colors


class Monitor(Devices):
    def __init__(self, brand: str, model: str, cost: float, resolution: str):
        super().__init__("Monitor", brand, model, cost)
        self.resolution = resolution


laptop_1 = Laptop("Apple", "13 air", 50000, "Mini")
laptop_2 = Laptop("HP", "GT100", 25000, "Desktop")

scanner_1 = Scanner("AOC", "CP100", 10000, "Colour")
scanner_2 = Scanner("Asos", "GT01", 5000, "B&W")

xerox_1 = Monitor("AOC", "UT100", 10000, "1200 x 1400")
xerox_2 = Monitor("HP", "SN01", 20000, "1200 x 1400")

store = Storage()

store.receive(laptop_1)
store.receive(laptop_2)
store.receive(scanner_1)
store.receive(scanner_2)
store.receive(scanner_2)

store.result_dict()
