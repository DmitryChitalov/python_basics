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
        print("Запуск отрисовки!")


class Pen(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки ручкой!")


class Pencil(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки карандашом!")


class Handle(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки маркером!")


s = Stationery('Канцелярия')
p = Pen('Ручка')
pe = Pencil('Карандаш')
h = Handle('Маркер')

print(s.title)
s.draw()

print(p.title)
p.draw()

print(pe.title)
pe.draw()

print(h.title)
h.draw()
