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
    """info"""
    title: str
    _message = "Запуск отрисовки."

    def draw(self):
        """info"""
        print(self._message)


class Pen(Stationery):
    """info"""
    title = 'Ручка'
    _message = f"{title} - рисует в тетрадке."


class Pencil(Stationery):
    """info"""
    title = 'Карандаш'
    _message = f"{title} - рисует на листке."


class Handle(Stationery):
    """info"""
    title = 'Маркер'
    _message = f"{title} - рисует на доске."


items = [Pen(), Pencil(), Handle()]

for item in items:
    item.draw()
