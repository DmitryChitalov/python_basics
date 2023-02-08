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
        print(f'Запуск отрисовки ручки - {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандаша - {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркера - {self.title}')

# проверка методов
stationery1 = Stationery("Ластик")
stationery1.draw()

pen1 = Pen("Черная ручка")
pen1.draw()

pen2 = Pen("Зеленая ручка")
pen2.draw()

pencil1 = Pencil("Простой карандаш")
pencil1.draw()

handle1 = Handle("Синий маркер")
handle1.draw()
