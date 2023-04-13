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
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def __init__(self):
        super().__init__("Pen")

    def draw(self):
        print(f"Run. {self.title}")


class Pencil(Stationery):

    def __init__(self):
        super().__init__("Pencil")

    def draw(self):
        print(f"Start. {self.title}")


class Handle(Stationery):

    def __init__(self):
        super().__init__("Marker")

    def draw(self):
        print(f"Launch. {self.title}")


my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()


