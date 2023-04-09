class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Отрисовка ручкой {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Отрисовка карандашом {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Отрисовка маркером {self.title}")


pen = Pen("синяя")
pencil = Pencil("черный")
handle = Handle("зеленый")

pen.draw()
pencil.draw()
handle.draw()