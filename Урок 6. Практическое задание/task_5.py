class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Запуск отрисовки"


class Pen(Stationery):
    def draw(self):
        return "Идёт отрисовка ручкой"


class Pencil(Stationery):
    def draw(self):
        return "Процесс отрисовки карандашём"


class Handle(Stationery):
    def draw(self, ):
        return "Запуск обработки маркером"


a = Pencil("карандашём")
b = Pen("ручкой")
c = Handle("маркер")

print(a.draw())
print(c.draw())
print(b.draw())
