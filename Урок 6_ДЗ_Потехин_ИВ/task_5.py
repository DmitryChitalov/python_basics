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
        return f'Предмет {self.title}. Отрисовка.'


# дочерние классы
class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
# переопределяем метод draw
    def draw(self):
        return f'Взяли пердмет - "{self.title}". Запуск отрисовки ручкой.'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Взяли пердмет - "{self.title}". Запуск отрисовки карандашом.'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Взяли предмет -  "{self.title}". Запуск отрисовки маркером.'

# клиентский код
pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
s = Stationery('чернила')
print(s.draw())
