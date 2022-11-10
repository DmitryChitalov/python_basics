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
        print('Запуск отрисовки.')
class Pen(Stationery):
    def draw(self):
        print(f'Рисуем ручкой {self.title}')
class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем карандашом {self.title}')
class Handle(Stationery):
    def draw(self):
        print(f'Рисуем маркером {self.title}')

p1 = Pen('Bic')
p2 = Pencil('Carioca')
p3 = Handle('Jimbo')
p1.draw()
p2.draw()
p3.draw()