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
        print('Запуск отрисовки:')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой: {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск прорисовки карандашом: {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером: {self.title}')

# проводим проверку методов
ps_1_pen = Pen("розовой ручкой")
ps_2_pen = Pen("красной ручкой")
ps_1_penс = Pencil("синим карандашом")
ps_2_penс = Pencil("желтым карандашом")
ps_han = Handle("черным маркером")

ps_1_pen.draw()
ps_2_pen.draw()
ps_1_penс.draw()
ps_2_penс.draw()
ps_han.draw()
