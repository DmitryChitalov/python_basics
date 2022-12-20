class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Инструмент - ручка")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Инструмент - карандаш")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Инструмент - маркер")

p = Pencil('BIC')
p.draw()
r = Pen('Gold')
r.draw()
c = Handle('Edding')
c.draw()