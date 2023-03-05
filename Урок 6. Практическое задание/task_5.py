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
    title = 'called'

    def draw(self):
        print('Запуск отрисовки')

class Pencil(Stationery):

    def draw(self):
        print(f'Сейчас будет рисовать {self.title}')

class Pen(Stationery):

    def draw(self):
        print('Давай что-нибудь напишем!')

class Handle(Stationery):

    def draw(self):
        print('Этим можно подчеркнуть.')

my_pencil = Pencil()
my_pencil.title = 'карандаш'
my_pencil.draw()

my_pen = Pen()
my_pen.draw()

my_handle = Handle()
my_handle.draw()
