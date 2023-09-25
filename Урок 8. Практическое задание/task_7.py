"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
class NoSpace(Exception):
    txt = "There is no free space in this stock"

    def __str__(self):
        return self.txt


class UnknownItem(Exception):
    txt = "I don't know this item"

    def __str__(self):
        return self.txt


class NotInt(Exception):
    txt = "PROBLEM!!!! Value can't be converted to int"

    def __str__(self):
        return self.txt

class Stock:
    list_of_equipment = {
        'Printer': [],
        'Scaner': [],
        'Copier': []
    }

    def __init__(self, size):
        self.size = size

    def add_to_stock(self, item):
        if self.size > 0:
            if item.class_name() == 'Printer':
                self.list_of_equipment['Printer'].append(item)
                self.size -= 1
            elif item.class_name() == 'Scaner':
                self.list_of_equipment['Scaner'].append(item)
                self.size -= 1
            elif item.class_name() == 'Copier':
                self.list_of_equipment['Scaner'].append(item)
                self.size -= 1
            else:
                raise UnknownItem
        else:
            raise NoSpace
        return "item was successfully added"

    def take_of_item(self, item):
        if item.class_name() == 'Printer':
            self.list_of_equipment['Printer'].remove(item)
            self.size += 1
        elif item.class_name() == 'Scaner':
            self.list_of_equipment['Scaner'].remove(item)
            self.size += 1
        elif item.class_name() == 'Copier':
            self.list_of_equipment['Scaner'].remove(item)
            self.size += 1
        else:
            raise UnknownItem

    def show_equipment(self):
        res = "There are in stock: \n"
        for key in self.list_of_equipment:
            if len(self.list_of_equipment[key]) > 0:
                res += f"{key}s = {len(self.list_of_equipment[key])} \n"
                res += "models are: \n"
                for el in self.list_of_equipment[key]:
                    res += f"{el.firm_name} model {el.model} \n"
            else:
                res += f"{key} no in stock\n"
        return res


class Equipment:
    voltage = 220

    def __init__(self, name, model):
        self.firm_name = name
        self.model = model

    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return self.firm_name


class Printer(Equipment):
    paper_size = 'A3'
    pass


class Copier(Equipment):
    color = False
    pass


class Scaner(Equipment):
    scan_speed_list_per_minute = 10
    pass

go_on = True
stock_capisity = input("Please enter stock capasity, or enter 'cancel'")
while go_on:
    try:
        if stock_capisity == 'cancel':
            break
        else:
            if stock_capisity.isnumeric():
                stock = Stock(int(stock_capisity))
                go_on = False
            else:
                raise NotInt
    except NotInt as e:
        print(e)

try:
    pr1 = Printer("HP", 'ls-1010')
    stock.add_to_stock(pr1)
    print(stock.show_equipment())
    pr2 = Printer("Keosera", '2323')
    stock.add_to_stock(pr2)
    print(stock.show_equipment())
    scaners = [['lenovo', '2324'], ['LG', '234-5'], ['Samsung', 'sg-123']]
    for el in scaners:
        stock.add_to_stock(Scaner(el[0],el[1]))
    print(stock.show_equipment())
    print("_____________")
    stock.take_of_item(pr2)
    print(stock.show_equipment())
except (NoSpace, UnknownItem) as e:
        print(e)
