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

class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Запуск отрисовки"

class Pen(Stationery): #ручка
    def draw(self):
        return "Запуск рисунка ручкой"

class Pencil(Stationery): #карандаш
    def draw(self):
        return "Запуск рисунка карандашом"

class Handle(Stationery): #маркер
    def draw(self):
        return "Запуск рисунка маркером"

ruchka = Pen("Ручка")
print(ruchka.draw())
karandash = Pencil("Карандаш")
print(karandash.draw())
marker = Handle("Маркер")
print(marker.draw())

