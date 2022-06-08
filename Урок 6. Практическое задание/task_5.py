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
    def __init__(self):
        self.title = self.__str__().split()[0][10:]
    
    def draw(self):
        return print('Draw smth')

class Pen(Stationery):
    def draw(self):
        return print('Blue ink line')

class Pencil(Stationery):
    def draw(self):
        return print('Gray line')

class Handle(Stationery):
    def draw(self):
        return print('Thick line')

pen = Pen()
print('\n', pen.title)
pen.draw()

pencil = Pencil()
print('\n', pencil.title)
pencil.draw()

handle = Handle()
print('\n', handle.title)
handle.draw()