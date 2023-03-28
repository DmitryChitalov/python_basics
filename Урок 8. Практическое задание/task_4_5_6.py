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
class MyExceptions(Exception):
    def __init__(self, txt):
        self.txt = txt


# ----------------------------------------------------------------------------------------------------------------------
class Stock:
    names = []  # Хранение всех названий созданных подразделений, включая склад

    def __init__(self, name='stock'):
        if name in self.names:
            print('Такое подразделение уже существует.')
        else:
            self.names.append(name)  # Добавляем имя нового департамента в список имен
            self.name = name
            self.storage_number = 0  # Фиксируем нулевой ответственного хранения на складе/департаменте (не сквозной)
            self.instorage = {}  # Создаем словарь для информации об ответственном хранении

    def to_storage(self, stuff):
        # Первичное размещение техники (без перемещения "из")
        self.storage_number += 1
        stuff.assign_stock_number(self.storage_number)
        stuff.change_department(self.name)
        self.instorage[self.storage_number] = {'type': stuff.type, 'inventory number': stuff.inv_number,
                                               'year': stuff.year, 'model': stuff.model}

    def to_storage_from(self, stuff, from_dep):
        # Перемещение техники. Сначала проверяем была ли она там, откуда перемещаем
        check = False
        for x in list(from_dep.instorage.values()):
            if stuff.inv_number == x['inventory number']:
                check = True
                break
        if check:
            from_dep.from_storage(stuff)
            self.to_storage(stuff)
        else:
            print(f'В подразделении {from_dep.name} нет техники с инвентаризационным номером {stuff.inv_number}')

    def from_storage(self, stuff):
        # Списание техники с ответственного хранения
        self.instorage.pop(stuff.storage_number)
        stuff.assign_stock_number(-1)

    def __str__(self):
        # Распечатка ведомости ответственного хранения
        my_str = f'Сейчас в подразделении {self.name} находятся: \n'
        for key, value in self.instorage.items():
            my_str += f'Складской номер {key}: {value} \n'
        return f"{'*' * 50} \n {my_str}"


# ----------------------------------------------------------------------------------------------------------------------
class OfficeEq:
    inv_numbers = []

    def __init__(self, inv_number, year, model):
        try:
            if inv_number in self.inv_numbers:  # Проверяем новый инвентаризационный номер на существование
                self.inv_number = -inv_number
                OfficeEq.append_inv(-inv_number)
                raise MyExceptions('Такой инвентаризационный номер уже существует')
            self.inv_number = inv_number  # Инвентаризационный номер сквозной (в отличие от storage_number)
            OfficeEq.append_inv(inv_number)
            self.model = str(model)
            self.storage = -1  # Создаем атрибут для хранения объекта Stock
            self.storage_number = -1  # Номера ответственного хранения (может повторяться для разных департаментов)
            self.year = int(year)
            if 2019 < year or year < 2000:
                self.year = 2019
                raise MyExceptions(f'Не корректный год оргтехники {year}')

        except ValueError:
            print('Проверьте корректность данных')
        except MyExceptions as err:
            print(err.txt)

    @classmethod
    def append_inv(cls, inv_num):
        # Уникальные инвентаризационные номера храним в классе
        OfficeEq.inv_numbers.append(inv_num)

    def assign_stock_number(self, num):
        self.storage_number = num

    def change_department(self, storage):
        self.storage = storage


# ----------------------------------------------------------------------------------------------------------------------
class Printer(OfficeEq):
    def __init__(self, inv_number, year, model, storage):
        super().__init__(inv_number, year, model)
        self.type = 'printer'
        self.storage = storage
        storage.to_storage(self)  # При первичном создании объекта сразу назначаем ответственный департамент (склад)


# ----------------------------------------------------------------------------------------------------------------------
class Scanner(OfficeEq):
    def __init__(self, inv_number, year, model, storage):
        super().__init__(inv_number, year, model)
        self.type = 'scanner'
        self.storage = storage
        storage.to_storage(self)


# ----------------------------------------------------------------------------------------------------------------------
class Copier(OfficeEq):
    def __init__(self, inv_number, year, model, storage):
        super().__init__(inv_number, year, model)
        self.type = 'copier'
        self.storage = storage
        storage.to_storage(self)


# ----------------------------------------------------------------------------------------------------------------------
print('*' * 50)
stock = Stock()
it = Stock('IT')
users = Stock('Users')
print(Stock.names)

print('*' * 50)
copier1 = Copier(11, 2012, 'Samsung', stock)
print(f'Год первого ксерокса: {copier1.year}')
copier2 = Copier(13, 2018, 'Mi', stock)
print(f'Модель второго ксерокса: {copier2.model}')
printer1 = Printer(12, 2015, 'HP LaserJet', it)

print('*' * 50)
print(stock, it, users)

print('*' * 50)
print(list(stock.instorage.values()))
it.to_storage_from(copier1, stock)
users.to_storage_from(copier2, stock)
print(stock)
print(it)
print(users)
