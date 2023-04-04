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
    title = None
#    def __init__(self, title):
#        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    title = "ручка"

    def draw(self):
        print(f"Запуск отрисовки ручкой")


class Pencil(Stationery):
    title = "карандаш"

    def draw(self):
        print(f"Запуск отрисовки карандашом")


class Handle(Stationery):
    title = "маркер"

    def draw(self):
        print(f"Запуск отрисовки маркером ")

obj = Pen()
obj.draw()
obj = Pencil()
obj.draw()
obj = Handle()
obj.draw()
