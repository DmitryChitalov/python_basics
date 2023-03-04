class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Отрисовано ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Отрисовано карандашом')

class Handle(Stationery):
    def draw(self):
        print('Отрисовано маркером')

my_stationery = Stationery('Канцелярия')
my_pen = Pen('Ручка')
my_pencil = Pencil('Карандаш')
my_handle = Handle('Маркер')

my_stationery.draw()
my_pen.draw()
my_pencil.draw()
my_handle.draw()
