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
        print(f'\n Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'\n Вы выбрали канцелярскую принадлежность: {self.title}'
              f'\n Запуск отрисовки')


class Pencil(Stationery):
    def draw(self):
        print(f'\n Вы выбрали канцелярскую принадлежность: {self.title}'
              f'\n Запуск отрисовки')


class Handle(Stationery):
    def draw(self):
        print(f'\n Вы выбрали канцелярскую принадлежность: {self.title}'
              f'\n Запуск отрисовки')


test_st = Stationery('')
test_st.draw()

test_pen = Pen('Ручка')
test_pencil = Pencil('Карандаш')
test_handle = Handle('Маркер')

test_pen.draw()
test_pencil.draw()
test_handle.draw()
