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


class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Запуск письма")


class Pencil(Stationery):
    def draw(self):
        print("Запуск чертежа")


class Handle(Stationery):
    def draw(self):
        print("Запуск маркирования")


notbook = Stationery("Тетрадь для великих идей")
print(notbook.title)
notbook.draw()

quill = Pen("Перо для письма")
print(quill.title)
quill.draw()

simp_pencil = Pencil("Карандаш с мягким стержнем")
print(simp_pencil.title)
simp_pencil.draw()

alco_marker = Handle("Синий маркер на спирту")
print(alco_marker.title)
alco_marker.draw()


