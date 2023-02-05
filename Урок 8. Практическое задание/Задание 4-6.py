"""Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру, например словарь.
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
на уроках по ООП.
"""

"""Можно еще очень много чего создавать и фантазировать"""

dictionary = {}


class Warehouse:
    # def __init__(self, dict_class):
    #     self.dict_class = dict_class

    def __str__(self):
        return self


class Equipment:
    def __init__(self, typ, dep, quan):
        self.typ = typ
        self.dep = dep
        try:  # при вводе строки завершает программу с принтом
            self.quan = int(quan)
        except ValueError:
            print('Wrong integer. Run program again')
            exit()

    def income(self):
        if len(dictionary) == 0:
            dictionary[self.dep] = [[self.typ, self.quan]]
        else:
            for i in dictionary.keys():
                if self.dep not in dictionary.keys():
                    dictionary[self.dep] = [[self.typ, self.quan]]
                    break
                else:
                    dictionary[self.dep].append([self.typ, self.quan])
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
                    return f'In "{i}" we have {j[1]} printers, model - "{self.model}"'


class Xerox(Equipment):
    def __init__(self, model):
        self.model = model

    def get_xr(self):
        for i in dictionary:
            for j in dictionary[i]:
                if j[0] == 'xerox':
                    return f'In "{i}" we have {j[1]} xeroxes, model - "{self.model}"'


class Scanner(Equipment):
    def __init__(self, model):
        self.model = model

    def get_sc(self):
        for i in dictionary:
            for j in dictionary[i]:
                if j[0] == 'scanner':
                    return f'In "{i}" we have {j[1]} scanners, model - "{self.model}"'


# создаем департаменты с оргтехникой
s = Equipment('scanner', 'General', 29)
s.income()
x = Equipment('xerox', 'General', 15)
x.income()
p = Equipment('printer', 'Store', 55)
p.income()
xx = Equipment('xerox', 'Store', 15)
xx.income()
print(f'Before other actions we had in warehouse: {dictionary}')

# перемещаем между департаментами
Equipment.move('General', 'scanner', 'Store')
Equipment.move('Store', 'printer', 'General')
Equipment.move('General', 'xerox', 'Store')
print(f'After moving some equipment we have: {Warehouse.__str__(dictionary)}')

# в личных классах храним в каком департаменте, в каком количестве и какой модели оборудование есть
pr = Printer('Canon')
print(pr.get_pr())
xr = Xerox('Anon')
print(xr.get_xr())
sc = Scanner('Non')
print(sc.get_sc())

"""
Before other actions we had in warehouse: {'General': [['scanner', 29], ['xerox', 15]], 'Store': [['printer', 55], ['xerox', 15]]}
After moving some equipment we have: {'General': [['printer', 55]], 'Store': [['xerox', 30], ['scanner', 29]]}
In "General" we have 55 printers, model - "Canon"
In "Store" we have 30 xeroxes, model - "Anon"
In "Store" we have 29 scanners, model - "Non"
"""
