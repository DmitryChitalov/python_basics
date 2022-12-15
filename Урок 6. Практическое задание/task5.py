class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return "Запуск отрисовки"

class Pen(Stationery):
    def draw(self):
        return "Запуск отрисовки " + self.title

class Pencil(Stationery):
    def draw(self):
        return "Запуск отрисовки " + self.title

class Handle(Stationery):
    def draw(self):
        return "Запуск отрисовки " + self.title

a = Pen("Ручка")
b = Pencil("Карандаш")
c = Handle("Маркер")
print(a.draw())
print(b.draw())
print(c.draw())