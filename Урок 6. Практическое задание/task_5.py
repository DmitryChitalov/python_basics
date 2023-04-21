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
        return 'Запуск отрисовки.'


class Pen(Stationery):
    def __init__(self):
        super().__init__("Pen")

    def draw(self):
        return 'Запуск отрисовки Ручкой'


class Pencil(Stationery):
    def __init__(self):
        super().__init__("Pencil")

    def draw(self):
        return 'Запуск отрисовки Карандашом'


class Handle(Stationery):
    def __init__(self):
        super().__init__("Handle")

    def draw(self):
        return 'Запуск отрисовки Маркером'


obj_pen = Pen()
obj_pencil = Pencil()
obj_handle = Handle()

print(obj_pen.draw())
print(obj_pencil.draw())
print(obj_handle.draw())
