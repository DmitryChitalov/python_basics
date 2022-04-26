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

import re


class Stor:
    storage = []
    summary = {}
    pulled = []
    mag = {1: 'г. Москва, ул. Тверская, д. 18',
           2: 'г. Санкт-Петербург, ул. Морская, д. 2',
           3: 'г. Тула, ул. Ленина, д. 13'}

    def push(self, eqp):
        Stor.storage.append(str(eqp))
        a = re.findall(r'\w+', str(eqp))[0]
        if Stor.summary.get(a) is not None:
            Stor.summary[a] += 1
        else:
            self.summary.setdefault(eqp.typ, 1)

    def pull(self, eq_typ, quant, n_mag):
        for _ in range(quant):
            for item in self.storage:
                a = re.findall(r'\w+', item)[0]
                if a == eq_typ:
                    self.pulled.append([n_mag, item])
                    self.storage.remove(item)
                    self.summary[eq_typ] -= 1
                    break

    def report_mags(self, num):
        print(f'В магазин №{num} по адресу: {self.mag[num]} отправлено: ')
        for item in self.pulled:
            if item[0] == num:
                print(item[1])

    def report_items(self):
        for item in self.storage:
            print(item)

    def report_total(self):
        for key, val in self.summary.items():
            print(f'{key}: {val} шт')


class Equip:

    def __init__(self, typ, inv, brand, model, cost, weight):
        self.typ = typ
        self.inv = inv
        self.brand = brand
        self.model = model
        self.cost = cost
        self.weight = weight

    @staticmethod
    def work():  # работа со складом
        while True:
            s1 = Stor()
            ex = input('Работа со складом. Для выхода - q, продолжить работу - Enter ---> ')
            if ex in ('Q', 'q'):
                exit()
            ex = input('Получаем товар на склад - I, отправляем в магазин - O, инфо по магазинам - M ---> ')
            if ex in ('I', 'i'):
                Equip.income()
                s1.report_items()
                s1.report_total()
            elif ex in ('O', 'o'):
                eq_typ = str(input('\nВведите тип оборудования (Принтер/Сканер/Копир): '))
                if eq_typ not in ('Принтер', 'Сканер', 'Копир'):
                    raise OwnError('Вы ввели неверный тип оборудования')
                quant = int(input('Введите количество товара: '))
                n_mag = int(input('Введите номер магазина: '))
                s1.pull(eq_typ, quant, n_mag)
                s1.report_items()
                s1.report_total()
            elif ex in ('M', 'm'):
                mag = int(input('Введите номер магазина (1-3): '))
                if mag not in (1, 2, 3):
                    raise OwnError('Вы ввели неверный номер магазина')
                s1.report_mags(mag)

    @staticmethod
    def income():  # ввод данных пользователем
        try:
            typ = str(input('\nВведите тип оборудования (Принтер/Сканер/Копир): '))
            if typ not in ('Принтер', 'Сканер', 'Копир'):
                raise OwnError('Вы ввели неверный тип оборудования')
            if typ == 'Принтер':
                inv = int(input('Введите инв. номер: '))
                brand = str(input('Введите производителя: '))
                model = str(input('Введите модель: '))
                cost = float(input('Введите цену: '))
                weight = float(input('Введите вес: '))
                clr = str(input('Введите цветность (цв/чб): '))
                if clr not in ('цв', 'чб'):
                    raise OwnError('Вы ввели неверную цветность')
                form = str(input('Введите формат бумаги: '))
                Stor.storage.append(str(Printer(inv, brand, model, cost, weight, clr, form)))
                if Stor.summary.get(typ) is not None:
                    Stor.summary[typ] += 1
                else:
                    Stor.summary.setdefault(typ, 1)
            elif typ == 'Сканер':
                inv = int(input('Введите инв. номер: '))
                brand = str(input('Введите производителя: '))
                model = str(input('Введите модель: '))
                cost = float(input('Введите цену: '))
                weight = float(input('Введите вес: '))
                dpi = int(input('Введите разрешение: '))
                Stor.storage.append(str(Scanner(inv, brand, model, cost, weight, dpi)))
                if Stor.summary.get(typ) is not None:
                    Stor.summary[typ] += 1
                else:
                    Stor.summary.setdefault(typ, 1)
            elif typ == 'Копир':
                inv = int(input('Введите инв. номер: '))
                brand = str(input('Введите производителя: '))
                model = str(input('Введите модель: '))
                cost = float(input('Введите цену: '))
                weight = float(input('Введите вес: '))
                spd = str(input('Введите скорость копирования: '))
                Stor.storage.append(str(Copier(inv, brand, model, cost, weight, spd)))
                if Stor.summary.get(typ) is not None:
                    Stor.summary[typ] += 1
                else:
                    Stor.summary.setdefault(typ, 1)
        except ValueError:
            print('Недопустимое значение!')
        except OwnError as err:
            print(err)


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Printer(Equip):
    def __init__(self, inv, brand, model, cost, weight, clr, form):
        super().__init__('Принтер', inv, brand, model, cost, weight)
        self.clr = clr
        self.form = form

    def __str__(self):
        return f'Принтер: производитель - {self.brand}, модель -  {self.model},' \
               f' цветность - {self.clr}, формат бумаги - {self.form},' \
               f' вес - {self.weight} кг, цена - {self.cost} руб., инв. номер - {self.inv}'


class Scanner(Equip):
    def __init__(self, inv, brand, model, cost, weight, dpi):
        super().__init__('Сканер', inv, brand, model, cost, weight)
        self.dpi = dpi

    def __str__(self):
        return f'Сканер: производитель - {self.brand}, модель -  {self.model},' \
               f' разрешение - {self.dpi} точек/дюйм, вес - {self.weight} кг,' \
               f' цена - {self.cost} руб., инв. номер - {self.inv}'


class Copier(Equip):
    def __init__(self, inv, brand, model, cost, weight, spd):
        super().__init__('Копир', inv, brand, model, cost, weight)
        self.spd = spd

    def __str__(self):
        return f'Копир: производитель - {self.brand}, модель -  {self.model},' \
               f' скорость копирования - {self.spd} стр/м,' f' вес - {self.weight} кг,' \
               f' цена - {self.cost} руб., инв. номер - {self.inv}'


# создаём экземпляры
printer1 = Printer(123545, 'HP', 'LJ 1200', 5400.65, 4, 'цв', 'A4')
copier3 = Copier(2353456, 'Xerox', 'OfficeWork5', 8500, 5, '20')
printer2 = Printer(3463447, 'Canon', 'F3+', 1500, 4, 'чб', 'A3')
scanner1 = Scanner(2353455, 'Epson', 'Perfection 24', 5500, 5, 2400)
copier1 = Copier(2353457, 'Brother', 'MegaPro4', 7350.75, 5, '24')
copier2 = Copier(767373, 'Xerox', 'Work Pro 12', 12800.50, 3, '48')
s = Stor()
# помещаем товар на склад
s.push(printer1)
s.push(copier3)
s.push(printer2)
s.push(scanner1)
s.push(copier1)
s.push(copier2)
print('Добро пожаловать на склад!\nУ нас есть в наличии товар:')
s.report_items()
s.report_total()

# начинаем интерактивную работу со складом
Equip.work()
