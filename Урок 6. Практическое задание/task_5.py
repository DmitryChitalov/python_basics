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
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки (ручка)")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки (карандаш)")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки (маркер)")


obj = Stationery()
obj.draw()

obj = Pen()
obj.draw()

obj = Pencil()
obj.draw()

obj = Handle()
obj.draw()
