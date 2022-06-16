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
        return print(f'Stationery {self.title}')


class Pen(Stationery):
    def draw(self):
        return print(f'Pen {self.title}')


class Pencil(Stationery):
    def draw(self):
        return print(f'Pencil {self.title}')


class Handle(Stationery):
    def draw(self):
        return print(f'Handle {self.title}')


pen = Pen('draw')
pen.draw()

pencil = Pencil('draw')
pencil.draw()

handle = Handle('draw')
handle.draw()
