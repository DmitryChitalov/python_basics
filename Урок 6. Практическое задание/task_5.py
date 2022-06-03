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
    _title: str

    def __init__(self):
        self._title = 'Unknown stationery'

    def draw(self):
        return f'Start rendering with {self._title}'


class Pen(Stationery):
    def __init__(self):
        self._title = "Pen"

    def draw(self):
        return f'You took the {self._title}. {super().draw()}'


class Pencil(Stationery):
    def __init__(self):
        self._title = "Pencil"

    def draw(self):
        return f'You took the {self._title}. {super().draw()}'


class Handle(Stationery):
    def __init__(self):
        self._title = "Handle"

    def draw(self):
        return f'You took the {self._title}. {super().draw()}'


stationery = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()
print(stationery.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())
