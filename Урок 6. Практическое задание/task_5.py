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
    title = ''

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    title = "Pen (ручка)"

    def draw(self):
        print(f"Запуск отрисовки {self.title}.")


class Pencil(Stationery):
    title = "Pencil (карандаш)"

    def draw(self):
        print(f"Запуск отрисовки {self.title}.")


class Handle(Stationery):
    title = "Handle (маркер)"

    def draw(self):
        print(f"Запуск отрисовки {self.title}.")


paint = Stationery()
paint.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
