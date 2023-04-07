"""
Задание 5.

Реализовать класс Stationery (канцелярская принадлежность).

Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”

Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).

В каждом из классов реализовать переопределение метода draw.

Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, in_title):
        self.title = in_title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self, in_title):
        super().__init__(in_title)

    def draw(self):
        print(f"Начали рисовать ручкой {self.title}")


class Pencil(Stationery):
    def __init__(self, in_title):
        super().__init__(in_title)

    def draw(self):
        print(f"Начали рисовать карандашом {self.title}")


class Handle(Stationery):
    def __init__(self, in_title):
        super().__init__(in_title)

    def draw(self):
        print(f"Начали рисовать маркером {self.title}")


obj_pen = Pen("pilot supergrip")
obj_pencil = Pencil("koch noor 3B")
obj_handle = Handle("PermanentM")

obj_pen.draw()
obj_pencil.draw()
obj_handle.draw()
