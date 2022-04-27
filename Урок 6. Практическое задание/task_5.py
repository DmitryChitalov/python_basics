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

from typing import List

class Stationery:
    title:str = None

    def __init__(self, title:str) -> None:
        if type(title) is str:
            self.title = title
        else:
            raise ValueError("The title of stationery must be as string.")

    def draw(self) -> None:
        print("Start drawing")



class Pen(Stationery):
    def __init__(self) -> None:
        super().__init__("Pen")

    def draw(self) -> None:
        print("Start pen drawing")



class Pencil(Stationery):
    def __init__(self) -> None:
        super().__init__("Pencil")

    def draw(self) -> None:
        print("Start pencil drawing")



class Handle(Stationery):
    def __init__(self) -> None:
        super().__init__("Handle")

    def draw(self) -> None:
        print("Start handle drawing")


stationeries:List[Stationery] = [
    Stationery("Empty"),
    Pen(),
    Pencil(),
    Handle()
]

for stationery in stationeries:
    stationery.draw()