'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''
dictionary = {}

class Storage:
    # def __init__(self, dict_class):
    #     self.dict_class = dict_class

    def __str__(self):
        return self

class Equipment:
    def __init__(self, typ, dep, quantity):
        self.typ = typ
        self.dep = dep
        #валидация вводимых пользователем значений кол-ва
        try:
            self.quantity = int(quantity)
        except ValueError:
            print('Неверное значение! Запустите программу снова.')
            exit()

    def income(self):
        if len(dictionary) == 0:
            dictionary[self.dep] = [[self.typ, self.quantity]]
        else:
            for i in dictionary.keys():
                if self.dep not in dictionary.keys():
                    dictionary[self.dep] = [[self.typ, self.quantity]]
                    break
                else:
                    dictionary[self.dep].append([self.typ, self.quantity])
                    break

    @staticmethod
    def move(fdep, fn, tdep):
        lst = []
        for m in dictionary[tdep]:
            lst.append(m[0])
        for i in dictionary[fdep]:
            if i[0] == fn:
                for j in dictionary[tdep]:
                    if j[0] == fn:
                        j[1] += i[1]
                        dictionary[fdep].remove(i)
                        break
            if fn not in lst:
                dictionary[tdep].append(i)
                dictionary[fdep].remove(i)
                break


class Printer(Equipment):
    def __init__(self, model):
        self.model = model

    def get_pr(self):
        for i in dictionary:
            for j in dictionary[i]:
                if j[0] == 'printer':
                    return f'На складе "{i}" имеется {j[1]} единиц оборудования: "printer", модели - "{self.model}"'


class Xerox(Equipment):
    def __init__(self, model):
        self.model = model

    def get_xr(self):
        for i in dictionary:
            for j in dictionary[i]:
                if j[0] == 'xerox':
                    return f'На складе "{i}" имеется {j[1]} единиц оборудования: "xerox", модели - "{self.model}"'


class Scanner(Equipment):
    def __init__(self, model):
        self.model = model

    def get_sc(self):
        for i in dictionary:
            for j in dictionary[i]:
                if j[0] == 'scanner':
                    return f'На складе "{i}" имеется {j[1]} единиц оборудования: "scanner", модели - "{self.model}"'

# создаем подразделения складов с оргтехникой
s = Equipment('scanner', 'Склад №1', input(f'Введите количество 1-го склада: '))
s.income()
x = Equipment('xerox', 'Склад №2', input(f'Введите количество 2-го склада: '))
x.income()
p = Equipment('printer', 'Склад №3', input(f'Введите количество 3-го склада: '))
p.income()
xx = Equipment('xerox', 'Склад №4', input(f'Введите количество 4-го склада: '))
xx.income()
pp = Equipment('printer', 'Склад №5', input(f'Введите количество 5-го склада: '))
pp.income()
print('*'*100)
print(f'Базовое состояние складов: {dictionary}')
# перемещаем оборудование между складами
print('*'*100)
Equipment.move('Склад №1', 'printer', 'Склад №2')
print(f'Выполняем перемещение оборудования', 'scanner', 'со склада №1 н склад №2')
Equipment.move('Склад №3', 'printer', 'Склад №5')
print(f'Выполняем перемещение оборудования', 'printer', 'со склада №3 н склад №5')
Equipment.move('Склад №2', 'xerox', 'Склад №4')
print(f'Выполняем перемещение оборудования', 'xerox', 'со склада №2 н склад №4')
print(f'Состояние складов после перемещения оборудования: {Storage.__str__(dictionary)}')
print('*'*100)
# в личных классах храним на каком складе, в каком количестве и какой модели оборудование есть
print(f'Распределение оборудования на складах')
pr = Printer('DCP-1610R')
print(pr.get_pr())
xr = Xerox('b310')
print(xr.get_xr())
sc = Scanner('HP-210')
print(sc.get_sc())
