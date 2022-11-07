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
    """
    базовый класс канцелярская принадлежность
    """
    def __init__(self, name) -> None:
        self.name = name

    def draw(self):
        """
        метод отрисовки
        """
        print("Запуск отрисовки.")

    def __str__(self) -> str:
        return self.name


class Pen(Stationery):
    """
    класс ручка
    """
    def __init__(self) -> None:
        super().__init__("Ручка")

    def draw(self):
        super().draw()
        print(f"Я пишу в тетради c помощью предмета {self.name}")


class Pencil(Stationery):
    """
    класс карандаш
    """
    def __init__(self) -> None:
        super().__init__("Карандаш")

    def draw(self):
        super().draw()
        print(f"Я рисую в альбоме с помощью {self.name}")


class Handle(Stationery):
    """
    класс маркер
    """
    def __init__(self) -> None:
        super().__init__("Маркер")

    def draw(self):
        super().draw()
        print(f"{self.name} рисует на доске")


tools = [Handle(), Pencil(), Pen()]

for tool in tools:
    tool.draw()
