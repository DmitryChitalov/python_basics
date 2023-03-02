# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад
# и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц
# оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).

class Store:
    def __init__(self):
        self.store = []

    def add(self, item: "OfficeStuff"):
        self.store.append(item)

    def transfer(self, idx: int, department: str):
        item: OfficeStuff = self.store[idx]
        item.department = department


class OfficeStuff:
    def __init__(self, name, model):
        self.name = name
        self.model = model


class Printer(OfficeStuff):
    def can_print(self):
        return f'может печатать'


class Scanner(OfficeStuff):
    def can_scan(self):
        return f'может сканировать'


class Copier(OfficeStuff):
    def can_copy(self):
        return f'может копировать'


store = Store()
store.add(Printer("Epson", "модель 1"))
store.add(Scanner("Cannon", "модель 1"))
store.add(Copier("Xerox", "модель 1"))
print(store)