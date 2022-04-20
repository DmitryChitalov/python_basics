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
    title = 'название'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Pen')


class Pencil(Stationery):
    def draw(self):
        print('Pencil')


class Handle(Stationery):
    def draw(self):
        print('Handle')


p = Stationery()
p.draw()
p1 = Pen()
p1.draw()
p2 = Pencil()
p2.draw()
p3 = Handle()
p3.draw()
