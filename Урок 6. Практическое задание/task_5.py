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
    title: str

    def __init__(self, my_title):
        self.title = my_title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки. Инструмент - {self.title} (Pen)")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки. Инструмент - {self.title} (Pencil)")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки. Инструмент - {self.title} (Handle)")


my_pen = Pen("карандаш")
my_pencil = Pencil("ручка")
my_handle = Handle("маркер")

my_pen.draw()
my_pencil.draw()
my_handle.draw()

