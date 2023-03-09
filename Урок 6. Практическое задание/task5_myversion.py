"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра
"""


class Stationery:
    # атрибут родительского класса
    def __init__(self, title):
        self.title = title

    # метод родительского класса
    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    # метод дочернего класса
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pencil(Stationery):
    # метод дочернего класса
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Handle(Stationery):
    # метод дочернего класса
    def draw(self):
        return f'Запуск отрисовки {self.title}'


pen = Pen('ручкой')
print(pen.draw())
pencil = Pencil('карандашем')
print(pencil.draw())
handle = Handle('маркером')
print(handle.draw())
