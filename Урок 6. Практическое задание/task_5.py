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
        print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self):
        super().__init__('ручкой')

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pencil(Stationery):

    def __init__(self):
        super().__init__('карандашом')

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Handle(Stationery):

    def __init__(self):
        super().__init__('маркером')

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


if __name__ == '__main__':
    p = Pen()
    n = Pencil()
    h = Handle()
    s = Stationery('канцелярская принадлежность')

    p.draw()
    n.draw()
    h.draw()
    s.draw()