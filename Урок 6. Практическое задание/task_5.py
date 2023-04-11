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
    def __init__(self, name):
        self.name = name

    def draw(self):
        return "Запуск отрисовки."


class Pen(Stationery):
    def draw(self):
        return f"Картина {self.name} - Отрисовка ручкой"


class Pencil(Stationery):
    def draw(self):
        return f"Картина {self.name} - Отрисовка карандашом"


class Handle(Stationery):
    def draw(self):
        return f"Картина {self.name} - Отрисовка маркером"


a = Pen("Лесные жители")
b = Pencil("Подводный мир")
c = Handle("Одиссея")

print(a.draw())
print(b.draw())
print(c.draw())
