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
    """
    канцелярская принадлежность

    Attributes:
        title   название
    """

    title = ''

    def draw(self):
        """
        Метод выводит сообщение 'Запуск отрисовки.'
        :return: 'Запуск отрисовки'
        """
        return 'Запуск отрисовки'


class Pen(Stationery):
    """
    ручка
    """
    def draw(self):
        """
        переопределяет метод draw
        :return: 'Линия ручкой'
        """
        return 'Линия ручкой'


class Pencil(Stationery):
    """
    карандаш
    """
    def draw(self):
        """
        переопределяет метод draw
        :return: 'окружность карандашом'
        """
        return 'окружность карандашом'


class Handle(Stationery):
    """
    маркер
    """
    def draw(self):
        """
        переопределяет метод draw
        :return: 'дуга маркером'
        """
        return 'дуга маркером'


stationery = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()

print(stationery.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())
