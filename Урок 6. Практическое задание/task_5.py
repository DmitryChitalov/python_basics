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
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Написание ручкой')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Рисование карандашом')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Рисование маркером')


pen1 = Pen("Шариковая ручка")
print(pen1.draw())
pencil5 = Pencil('Простой карандаш 2М')
print(pencil5.draw())
handle1 = Handle('Зеленый маркер')
print(handle1.draw())

pen3 = Pen('Гелевая ручка')
print(f'Надо написать название с помощью: {pen3.title}')
print(f'Надо выделить местоимения с помощью: {handle1.title}')
