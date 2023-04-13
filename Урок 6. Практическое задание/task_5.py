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
    title = ''

    def draw(self):
        pass


class Pen(Stationery):
    def draw(self):
        print(f"Draw '{self.title}' by Pen")


class Pencil(Stationery):
    def draw(self):
        print(f"Draw '{self.title}' by Pencil")


class Handle(Stationery):
    def draw(self):
        print(f"Draw '{self.title}' by Handle")


pen = Pen()
pen.title = 'Story book'
pen.draw()

pencil = Pencil()
pencil.title = 'draft'
pencil.draw()

handle = Handle()
handle.title = 'PERMANENT'
handle.draw()
