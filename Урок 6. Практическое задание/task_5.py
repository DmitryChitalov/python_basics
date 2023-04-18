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
        print('Starting to draw')
    
class Pen(Stationery):
    def draw(self):
        print('Starting to draw with a pen')
    
class Pencil(Stationery):
    def draw(self):
        print('Starting to draw with a pencil')

class Marker(Stationery):
    def draw(self):
        print('Starting to draw with a marker')

pen = Pen('Red pen')
pen.draw()
marker = Marker('Green marker')
marker.draw()
