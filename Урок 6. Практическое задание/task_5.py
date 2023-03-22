class Stationery:
    title = str("Канцелярия")
    b = str(" ")

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    b = str("Ручка")

    def draw(self):
        print(f"{self.title} - {self.b} ... Запуск отрисовки.")


class Pencil(Stationery):
    b = str("Карандаш")

    def draw(self):
        print(f"{self.title} - {self.b} ... Запуск отрисовки.")


class Handle(Stationery):
    b = str("Маркер")

    def draw(self):
        print(f"{self.title} - {self.b} ... Запуск отрисовки.")


a = Pen()
a.draw()

a = Pencil()
a.draw()

a = Handle()
a.draw()

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
