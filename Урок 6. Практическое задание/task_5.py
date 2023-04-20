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
        print("Запуск отрисовки, ", end='')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print(f"инструмент: {self.title}, главное не ошибиться - не сотрешь")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print(f"инструмент: {self.title}, ошибиться не боимся")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print(f"инструмент: {self.title}, точно не сотрешь")


my_pen = Pen('Ручка')
my_pencil = Pencil('Карандаш')
my_handle = Handle('Маркер')
my_pen.draw()
my_pencil.draw()
my_handle.draw()
