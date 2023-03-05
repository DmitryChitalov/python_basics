"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные
атрибуты: speed, color, name, is_police (булево).

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

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} равна {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} в городе  равна {self.speed}')

        if self.speed > 60:
            return f'{self.name} превышает скоростной режим в городе'
        else:
            return f'{self.name} скоростной режим в городе сооблюдает'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость в городе {self.name} равна {self.speed}')

        if self.speed > 40:
            return f'{self.name} превышает скоростной режим в городе'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейский авто'
        else:
            return f'{self.name} не полицейский авто'


Audi_R8 = SportCar(174, 'Желтый', 'Audi_R8', False)
LADA_Granta = TownCar(61, 'Черная', 'LADA_Granta', False)
ГАЗель_Next = WorkCar(35, 'Белая', 'ГАЗель_Next', False)
Lada_Vesta = PoliceCar(120, 'Себристый',  'Lada_Vesta', True)
print(Audi_R8.turn_left())
print(f'Когда {LADA_Granta.turn_right()}, {Audi_R8.stop()}')
print(f'{ГАЗель_Next.go()} со скоростью {ГАЗель_Next.show_speed()}')
print(f'{LADA_Granta.name} {LADA_Granta.color}')
print(f'{ГАЗель_Next.name} полицейская машина? {ГАЗель_Next.is_police}')
print(f'{Audi_R8.name} полицейская машина? {Audi_R8.is_police}')
print(ГАЗель_Next.show_speed())
print(Audi_R8.show_speed())
print(Lada_Vesta.police())
print(LADA_Granta.show_speed())