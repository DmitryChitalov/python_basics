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
    title = "Канцелярская принадлежность"

    def draw(self):
        print("Запуск отрисовки:")


class Pen(Stationery):
    def draw(self):
        print("Пишем ручкой.")


class Pencil(Stationery):
    def draw(self):
        print("Рисуем карандашом.")


class Handle(Stationery):
    def draw(self):
        print("Закрашиваем маркером.")


stationery = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
