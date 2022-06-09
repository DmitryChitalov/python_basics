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
class Stationary:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        print('Запуск отрисовки')


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Отрисовка {self.title}. Класс Pen')


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Отрисовка {self.title}. Класс Pencil')


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Отрисовка {self.title}. Класс Handle')


p_obj = Pen('ручкой')
pc_obj = Pencil('карандашом')
h_obj = Handle('маркером')

p_obj.draw()
pc_obj.draw()
h_obj.draw()
