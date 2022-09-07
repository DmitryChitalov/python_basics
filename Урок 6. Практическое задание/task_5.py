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
    title = ""

    def draw(self):
        print("Запуск отрисовки")

    def __init__(self):
        self.draw()


class Pen(Stationery):

    def draw(self):
        print("Ручка пишет")

    def __init__(self):
        super().__init__()
        self.title = "Pen"


class Pencil(Stationery):

    def draw(self):
        print("Карандаш чертит")

    def __init__(self):
        super().__init__()
        self.title = "Pencil"


class Handle(Stationery):

    def draw(self):
        print("Маркер обводит")

    def __init__(self):
        super().__init__()
        self.title = "Handle"


pen = Pen()
pencil = Pencil()
handle = Handle()
