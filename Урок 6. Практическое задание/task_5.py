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
        return "Запуск отрисовки: "

class Pen(Stationery):
    def draw(self):
        return "Запуск отрисовки: " + self.title

class Pencil(Stationery):
    def draw(self):
        return "Запуск отрисовки: " + self.title

class Handle(Stationery):
    def draw(self):
        return "Запуск отрисовки: " + self.title

a = Pen("ручка")
b = Pencil("карандаш")
c = Handle("маркер")
print(a.draw())
print(b.draw())
print(c.draw())
