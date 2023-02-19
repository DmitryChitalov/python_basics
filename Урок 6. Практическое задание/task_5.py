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
        print("Запуск отрисовки")

class Pen(Stationery):
    def __init__(self, title="pen"):
        super().__init__(title)
    def draw(self):
        print(f"{self.title} Запуск отрисовки ручкой")

class Pencil(Stationery):
    def __init__(self, title="pencil"):
        super().__init__(title)
    def draw(self):
        print(f"{self.title} Запуск отрисовки карандашом")

class Handle(Stationery):
    def __init__(self, title="handle"):
        super().__init__(title)
    def draw(self):
        print(f"{self.title} Запуск отрисовки маркером")

pen = Pen()
pen.draw()
pencil = Pencil("карандаш")
pencil.draw()
handle = Handle("handle")
handle.draw()
