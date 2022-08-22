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
class Statoinery():

    def __init__(self, title = 'ABC'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Statoinery):

    def draw(self):
        self.title = 'pen'
        return print(f'{self.title}. Запуск отрисоввки')


class Pencil(Statoinery):

    def draw(self):
        self.title = 'Pencil'
        return print(f'{self.title}. Запуск отрисоввки')

class Handle(Statoinery):

    def draw(self):
        self.title = 'Handle'
        return print(f'{self.title}. Запуск отрисоввки')

a = Pen()
a.draw()
a = Pencil()
a.draw()
a = Handle()
a.draw()
a = Statoinery()
a.draw()