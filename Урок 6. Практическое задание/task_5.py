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

    def draw(self):
        print("Start_rendering")


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "Uses Pen"


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "Uses Pencil"


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "Uses Handle"


pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
