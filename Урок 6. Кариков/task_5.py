
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Отрисовка {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Отрисовка {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Отрисовка {self.title}'


pen = Pen('ручкой')
print(pen.draw())
pencil = Pencil('карандашем')
print(pencil.draw())
handle = Handle('маркером')
print(handle.draw())