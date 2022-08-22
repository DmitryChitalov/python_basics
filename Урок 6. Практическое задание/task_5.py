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
    """ Канцелярская принадлежность """
    title = None

    def draw(self):
        """draw"""
        print("Запуск отрисовки.")


class Pen(Stationery):
    """Pen"""
    title = "Pen"

    def draw(self):
        """draw"""
        print(f"Запуск отрисовки {self.title}.")


class Pencil(Stationery):
    """Pencil"""
    title = "Pencil"

    def draw(self):
        """draw"""
        print(f"Запуск отрисовки {self.title}.")


class Handle(Stationery):
    """Handle"""
    title = "Handle"

    def draw(self):
        """draw"""
        print(f"Запуск отрисовки {self.title}.")


a = Stationery()
a.draw()
b = Pen()
b.draw()
c = Pencil()
c.draw()
d = Handle()
d.draw()
