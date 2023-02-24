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
        print(f"Запуск отрисовки {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title} ручкой ")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title} карандашём ")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки маркером {self.title}")


stationery = Stationery('перьевой ручкой')
stationery.draw()

pen = Pen('гелевой')
pen.draw()

pencil = Pencil('цветным')
pencil.draw()

handle = Handle('для белой доски')
handle.draw()