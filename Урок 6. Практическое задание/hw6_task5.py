class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        info_1 = "Запуск отрисовки\n"
        return info_1


class Pen(Stationery):
    def draw(self):
        pen_info = "Пишем ручкой\n"
        return pen_info


class Pencil(Stationery):
    def draw(self):
        pencil_info = "Чертим карандашом\n"
        return pencil_info


class Handle(Stationery):
    def draw(self):
        handle_info = "Выделяем маркером\n"
        return handle_info


p1 = Pen('ручка')
print(p1.draw())

p2 = Pencil('карандаш')
print(p2.draw())

h = Handle('маркер')
print(h.draw())
