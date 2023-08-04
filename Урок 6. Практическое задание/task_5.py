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
        print(f'Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title} ручкой.')

class Pencil(Stationery):
    def draw(self):
        print(f'Отрисовка карандашом {self.title}.')

class Handle(Stationery):
    def draw(self):
        print(f'{self.title} маркер, отрисовка. Запуск.')


stat = Stationery("")
stat.draw()
pen = Pen('кошки')
pen.draw()
pencil = Pencil('картинки')
pencil.draw()
handle = Handle('Красный')
handle.draw()