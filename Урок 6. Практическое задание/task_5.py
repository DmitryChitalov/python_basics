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

# pylint: disable=missing-class-docstring, missing-function-docstring


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки ручкой {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки карандашем {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки маркером {self.title}")


o = Stationery('')
o.draw()

pen = Pen('шариковой')
pen.draw()

pencil = Pencil('в тетраде')
pencil.draw()

handle = Handle('на доске')
handle.draw()
