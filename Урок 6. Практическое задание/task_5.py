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
        print(f"{self.title} Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}")


"""Создание классов"""
result_0 = Stationery("режим")
result_1 = Pen("ручкой")
result_2 = Pencil("карандашом")
result_3 = Handle("пальцем")
"""Вызов методов"""
result_0.draw()
result_1.draw()
result_2.draw()
result_3.draw()
