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
        print(f"Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {type(self).__name__}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {type(self).__name__}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {type(self).__name__}")


my_stationery = Stationery("Канцелярия")
my_stationery.draw()

my_pen = Pen("Ручка")
my_pen.draw()

my_pencil = Pencil("Карандаш")
my_pencil.draw()

my_handle = Handle("Маркер")
my_handle.draw()
