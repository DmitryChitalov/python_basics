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
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return 'Запуск отрисовки при помощи ручки(Pen) '


class Pencil(Stationery):
    def draw(self):
        return 'Запуск отрисовки при помощи карандаша'


class Handle(Stationery):
    def draw(self):
        return 'Запуск отрисовки при помощи ручки(Handle)'


a = Pen('Pen')
b = Pencil('Pencil')
c = Handle('Handle')
print(a.draw())
print(b.draw())
print(c.draw())
