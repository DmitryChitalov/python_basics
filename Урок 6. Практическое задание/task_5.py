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
from os import system, name as osname
from time import sleep


def cls():
    system('cls' if osname == 'nt' else 'clear')


class Stationery:
    def __init__(self, title=""):
        self.title = title

    def draw(self):
        return print(f"Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        title = "ручкой"
        return print(f"Запуск отрисовки {title}")


class Pencil(Stationery):
    def draw(self):
        title = "карандашем"
        return print(f"Запуск отрисовки {title}")


class Handle(Stationery):
    def draw(self):
        title = "маркером"
        return print(f"Запуск отрисовки {title}")


cls()
simple = Stationery()
pen = Pen()
pencil = Pencil()
marker = Handle()
simple.draw()
sleep(3)
pen.draw()
sleep(3)
pencil.draw()
sleep(3)
marker.draw()
sleep(3)
