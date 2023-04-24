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
import c1 as c1


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"{self.title} начинает рисовать")


class Pencil(Stationery):
    def draw(self):
        print(f"{self.title} начинает рисовать, можно стереть")


class Handle(Stationery):
    def draw(self):
        print(f"{self.title} начинает рисовать. Можно выделить текст")


a = Stationery("Перо")
b = Pen("Ручка")
c = Pencil("Карандаш")
d = Handle("Маркер")
a.draw()
b.draw()
c.draw()
d.draw()

