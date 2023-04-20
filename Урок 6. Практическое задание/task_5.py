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
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки с помощью {self.title} ручки')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки с помощью {self.title} карандаша')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки с помощью {self.title} маркера')


name = Stationery('Отрисовка')
print(name.title)
pen = Pen('синей')
pen.draw()
pencil = Pencil('мягкого')
pencil.draw()
handle = Handle('желтого')
handle.draw()
