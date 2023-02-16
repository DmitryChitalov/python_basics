class Stationery:
    def __init__(self):
        self.title = "Название"

    def draw(self):
        return "Отрисовка"


class Pen(Stationery):
    def draw(self):
        return "Запуск отрисовки ручкой"


class Pencil(Stationery):
    def draw(self):
        return "Запуск отрисовки карандашом"


class Handle(Stationery):
    def draw(self):
        return "Запуск отрисовки маркером"


abc = Stationery()
pen_1 = Pen()
pencil_1 = Pencil()
handle_1 = Handle()
print(abc.draw())
print(pen_1.draw())
print(pencil_1.draw())
print(handle_1.draw())