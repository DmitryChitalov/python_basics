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

# Выводим название
print(f'\nЗадание 5.\n')

# Объявляем классы и методы
class Stationery:
    title = 'Канцелярия'

    def draw(self):
        print('Запуск отрисовки.')

    def __init__(self):
        self.draw()

class Pen(Stationery):
    title = 'Ручка'
    def draw(self):
        print(f'Запуск отрисовки - {self.title}.')

class Pencil(Stationery):
    title = 'Карандаш'
    def draw(self):
        print(f'Запуск рисования - {self.title}.')


class Handle(Stationery):
    title = 'Маркер'
    def draw(self):
        print(f'Запуск выделения текста - {self.title}.')

# Объявляем переменные
stationary = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()
