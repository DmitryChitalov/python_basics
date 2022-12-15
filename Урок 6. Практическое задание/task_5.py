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


class Stationery:   # родительский класс
    def __init__(self, title):
        self.title = title

    def draw(self):     # определяем метод класса draw
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):  # дочерний класс
    def draw(self):     # переопределяем метод draw
        print(f'Пишет {self.title}')


class Pencil(Stationery):   # дочерний класс
    def draw(self):     # переопределяем метод draw
        print(f'Чертит {self.title}')


class Handle(Stationery):   # дочерний класс
    def draw(self):     # переопределяем метод draw
        print(f'Выделяет {self.title}')


st = Stationery('канцелярские принадлежности')
st.draw()
pn = Pen('ручка')
pn.draw()
pncl = Pencil('карандаш')
pncl.draw()
hndl = Handle('маркер')
hndl.draw()
