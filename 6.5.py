class Stationery:
    title: str
    _message = "Запуск отрисовки."

    def draw(self):
        print(self._message)


class Pen(Stationery):
    title = 'Ручка'
    _message = f"{title} - рисует в тетрадке."


class Pencil(Stationery):
    title = 'Карандаш'
    _message = f"{title} - рисует на листке."


class Handle(Stationery):
    title = 'Маркер'
    _message = f"{title} - рисует на доске."


items = [Pen(), Pencil(), Handle()]

for item in items:
    item.draw()