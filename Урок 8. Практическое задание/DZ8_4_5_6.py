class Warehouse:
    capacity = 100
    wh_dict = {'vendor': [],
               'model': [],
               'color': [],
               'size': [],
               'type': []}



    def __str__(self):
        return f'{self.wh_dict}'

    def load(self):
        wh_tmp = self.wh_dict.get('size')
        wh_load = 0
        for el in wh_tmp:
            wh_load += int(el)
        return int(wh_load)

    def checkcapacity(self):
        return self.capacity

    def emptycapacity(self):
        res = self.capacity - self.load()
        return int(res)

    def validation(self, *ars):
        try:
            if type(self.description.get('size')) != int:
                raise SizeErr
        except SizeErr as err:
            print(err)

    def reception(self, obj, *args):
        try:
            if int(self.description.get('size')) > obj.emptycapacity():
                raise FullCapacity
            for key in obj.wh_dict.keys():
                if key in self.description.keys():
                    val_list = obj.wh_dict.get(key)
                    tmp_list = []
                    for el in val_list:
                        if el == self.description.get(key) and key != 'size':
                            del el
                        else:
                            tmp_list.append(el)
                    tmp_list.append(self.description.get(key))
                    tmp_dict = {key: tmp_list}
                obj.wh_dict.update(tmp_dict)
            print(f'Добавлено на склад {obj}')
        except FullCapacity as err:
            print(err)


    def transport(self, department):
        self.description['transfer'] = department
        return print(f'{self} передано в {department}')

class FullCapacity(Exception):

    def __str__(self):
        return f'Склад переполнен!'

class SizeErr(Exception):

    def __str__(self):
        return f'Занимаемый размер указывается только в виде числа'

class OffEqu(Warehouse):

    def __init__(self, type, vendor, model, color, size):
        self.type = type
        self.vendor = vendor
        self.model = model
        self.color = color
        self.size = size
        self.description = {'vendor': self.vendor,
                            'model': self.model,
                            'color': self.color,
                            'size': self.size,
                            'type': self.type}


class Printer(OffEqu):

    def __init__(self, *args):
        super().__init__('printer', *args)

    def __str__(self):
        return f'{self.description}'

class Scanner(OffEqu):

    def __init__(self, *args):
        super().__init__('scaner', *args)

    def __str__(self):
        return f'{self.description}'
class Xerox(OffEqu):

    def __init__(self, *args):
        super().__init__('xerox', *args)

    def __str__(self):
        return f'{self.description}'

wh1 = Warehouse()
p1 = Printer('Epson', 'P132', 'black', 2)
p2 = Printer('Epson', 'P132', 'white', 2)
p3 = Printer('Canon', 'LBP20', 'grey', 6)

s = Scanner('Fujitsu', '6130', 'white', 4)
x = Xerox('Xerox', '301', 'white', '4')

p1.reception(wh1)
p2.reception(wh1)
p3.reception(wh1)
s.reception(wh1)
x.reception(wh1)
p3.transport('Логистика')
print(wh1.wh_dict)







