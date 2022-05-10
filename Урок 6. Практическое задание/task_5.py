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
    title = 'Title'

    def draw(self):
        print('Sorting start')


class Pen(Stationery):
    def draw(self):
        print('Pen draw')


class Pencil(Stationery):
    def draw(self):
        print('Pencil draw')


class Handle(Stationery):
    def draw(self):
        print('Handle draw')


my_pen = Pen()
my_pen.draw()
my_pencil = Pencil()
my_pencil.draw()
my_handle = Handle()
my_handle.draw()
