"""
Реализовать класс Stationery (канцелярская принадлежность). Определить
в нем атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
переопределение метода draw. Для каждого из классов методы должен
выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title: str

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    title = "ручка"

    def draw(self):
        print(f"{self.title} пишет")


class Pencil(Stationery):
    title = "карандаш"

    def draw(self):
        print(f"{self.title} чертит")


class Handle(Stationery):
    title = "маркер"

    def draw(self):
        print(f"{self.title} рисует")


if __name__ == '__main__':
    stationery = Stationery()
    stationery.draw()

    pen = Pen()
    pen.draw()

    pencil = Pencil()
    pencil.draw()

    handle = Handle()
    handle.draw()
