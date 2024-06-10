"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def show_speed(self):
        print(f'скорость автомобиля - {self.speed}')

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f'машина повернула на {direction}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'скорость автомобиля {self.name} - {self.speed}. Скорость превышена!')
        else:
            print(f'скорость автомобиля {self.name} - {self.speed}.')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'скорость автомобиля {self.name} - {self.speed}. Скорость превышена!')
        else:
            print(f'скорость автомобиля {self.name} - {self.speed}.')


class SportCar(Car):
    def sport(self):
        print(f"автомобиль {self.name} является спортивным.")


class PoliceCar(Car):
    def police(self):
        print(f"автомобиль {self.name} является полицейским.")


moskvich = TownCar(59, "зелёный", "Komby", False)
print(f'цвет автомобиля {moskvich.name} - {moskvich.color}.')
moskvich.go()
moskvich.show_speed()
moskvich.turn("север")
moskvich.stop()

traktor = WorkCar(45, "Синий", "Катюша", False)
print(f'автомобиль {traktor.name} является полицейским авто - {traktor.is_police}')
print(f'цвет автомобиля {traktor.name} - {traktor.color}.')
traktor.go()
traktor.show_speed()
traktor.turn("юг")
traktor.stop()

volga = PoliceCar(120, "белый", "Gaz 31", True)
volga.police()

bmv = SportCar(180, "красный", "Бумер", False)
bmv.sport()
