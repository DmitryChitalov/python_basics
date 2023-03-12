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
    def __init__(self, location, capacity):
        self.location = location
        self.capacity = capacity
        self.inventory = {}

    def add_item(self, item, quantity):
        if isinstance(quantity, int):
            if item in self.inventory:
                self.inventory[item] += quantity
            else:
                self.inventory[item] = quantity
            print(f"{quantity} {item} были добавлены на склад.")
        else:
            print("Количество должно быть целым числом.")

    def remove_item(self, item, quantity):
        if isinstance(quantity, int):
            if item in self.inventory:
                if self.inventory[item] >= quantity:
                    self.inventory[item] -= quantity
                    print(f"{quantity} {item} были удалены со склада.")
                    return True
                else:
                    print(f"Недостаточно {item} на складе.")
            else:
                print(f"{item} отсутствует в инвентаре склада.")
        else:
            print("Количество должно быть целым числом.")
        return False

    def transfer_item(self, item, quantity, department):
        if isinstance(quantity, int):
            if self.remove_item(item, quantity):
                print(f"{quantity} {item} было передано в {department}.")
                return True
            else:
                print(f"Передать {item} в {department} не удалось.")
                return False
        else:
            print("Количество должно быть целым числом.")

warehouse = Warehouse("Екатеринбург", 10)
warehouse.add_item("Принтер", 5)
warehouse.add_item("Сканер", 2)

print(warehouse.inventory) # {'Принтер': 5, 'Сканер': 2}

warehouse.transfer_item("Принтер", 3, "IT отдел")
print(warehouse.inventory) # {'Принтер': 2, 'Сканер': 2}

warehouse.transfer_item("Сканер", 4, "IT отдел")