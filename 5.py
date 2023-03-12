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
from abc import ABC, abstractmethod


class Stationery(ABC):
    def __init__(self, title: str):
        self.title = title

    @abstractmethod
    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Вы взяли {self.title}. Началась отрисовка ручкой.'


class Pencil(Stationery):
    def draw(self):
        return f'Вы взяли {self.title}. Началась отрисовка карандашом.'


class Handle(Stationery):
    def draw(self):
        return f'Вы взяли {self.title}. Началась отрисовка маркером.'


if __name__ == '__main__':
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    print(pen.draw())
    print(pencil.draw())
    print(handle.draw())
