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
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Отрисаовка {self.title}')
class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Отрисовка {self.title}')
class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Отрисовка {self.title}')

a = Stationery(None)
a.draw()
pen = Pen('ручкой')
pen.draw()
pencil = Pencil('карандашом')
pencil.draw()
handle = Handle('маркером')
handle.draw()
