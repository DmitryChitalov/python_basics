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
class stationery:
    title: str
    def draw(self):
        print(f'Запук отрисовки: ')
class Pen(stationery):
    title = 'Ручка'
    def draw(self):
        print(f'{self.title} - зачеркивает')
class Pencil(stationery):
     title = 'Карандаш'
     def draw(self):
         print(f'{self.title} - рисует')
class Handle(stationery):
     title = 'Маркер'
     def draw(self):
         print(f'{self.title} - подчеркивает ')

if __name__ == '__main__':
     stationery = stationery()
     stationery.draw()
     pen = Pen()
     pen.draw()
     pencil = Pencil()
     pencil.draw()
     handle = Handle()
     handle.draw()


