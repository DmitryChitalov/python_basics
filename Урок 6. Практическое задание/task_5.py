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
    title: str

    def draw(self):
        return print("Запуск отрисовки.")

    def __init__(self, title):
        self.title = title


class Pen(Stationery):
    def draw(self):
        return print(f"Запуск отрисовки. Используется {self.title}")


class Pencil(Stationery):
    def draw(self):
        return print(f"Запуск отрисовки. Используется {self.title}")


class Handle(Stationery):
    def draw(self):
        return print(f"Запуск отрисовки. Используется {self.title}")


pen = Pen("ручка")  # В скобках передаём title (название)
pen.draw()

pencil = Pencil("карандаш")
pencil.draw()

handle = Handle("маркер")
handle.draw()
