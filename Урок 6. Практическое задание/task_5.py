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
        return f'Запуск отрисовки'


class Pen(Stationery):

    def draw(self):
        return f'{self.title} - Запуск отрисовки'


class Pencil(Stationery):

    def draw(self):
        return f'{self.title} - Запуск отрисовки'


class Handle(Stationery):

    def draw(self):
        return f'{self.title} - Запуск отрисовки'


pen = Pen('Ручка')
print(pen.draw())

pencil = Pencil('Карандаш')
print(pencil.draw())

handle = Handle('Маркер')
print(handle.draw())
