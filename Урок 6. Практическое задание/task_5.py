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
        print('Запус отрисовки')


class Pen(Stationery):

    def draw(self):
        print('Запуск отрисовки:\nУникальное сообщение 1')


class Pencil(Stationery):

    def draw(self):
        print('Запуск отрисовки:\nУникальное сообщение 2')


class Handle(Stationery):

    def draw(self):
        print('Запуск отрисовки:\nУникальное сообщение 3')


pen_1 = Pen('Чёрная шариковая ручка')
pencil_1 = Pencil('Карандаш 2Н')
handle_1 = Handle('Розовый маркер')

print(pen_1.title)
pen_1.draw()

print(pencil_1.title)
pencil_1.draw()

print(handle_1.title)
handle_1.draw()

