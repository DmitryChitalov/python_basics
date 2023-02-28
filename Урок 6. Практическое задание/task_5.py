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
    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        Stationery.draw(self)
        print('Ручка пишет.')


class Pencil(Stationery):
    def draw(self):
        Stationery.draw(self)
        print('Карандаш ресует.')


class Handle(Stationery):
    def draw(self):
        Stationery.draw(self)
        print('Маркер выделяет.')


pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()
