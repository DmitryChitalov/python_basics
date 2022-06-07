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
    def __init__(self, name):
        self.title = name

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self, name):
        super().__init__(name)

    def draw(self):
        print('класс pen а имя ', self.title)


class Pencil(Stationery):
    def __init__(self, name):
        super().__init__(name)

    def draw(self):
        print('класс pencil  а имя ', self.title)

class Handle(Stationery):
    def __init__(self, name):
        super().__init__(name)

    def draw(self):
        print('класс handle а имя ' , self.title)


one = Stationery('канцелярия')
one.draw()
two = Pen('ручка')
two.draw()
tree = Pencil('карандаш')
tree.draw()
four = Handle('перо')
four.draw()