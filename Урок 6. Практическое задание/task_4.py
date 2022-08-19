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
class Car:
    '''Машина'''
    name = ''
    speed = 0
    color = 'white'
    is_police = False
    is_riding = False

    def __init__(self, name, speed, color = 'white'):
        self.name = name
        self.speed = speed
        self.color = color

    def go(self):
        '''старт'''
        self.is_riding = True
        return 'Машина поехала'

    def stop(self):
        '''остановка'''
        self.is_riding = False
        return 'Машина остановилась'

    def turn(self, direction):
        '''поворот'''
        return f'Машина повернула {direction}'

    def show_speed(self):
        '''Показ текущей скорости автомобиля'''
        if self.is_riding:
            return f'Текущая скорость автомобиля: {self.speed}'
        else:
            return 'Текущая скорость автомобиля: 0'

class TownCar(Car):
    '''городской автомобиль'''
    def show_speed(self):
        '''скорость для гр. авто'''
        if self.is_riding:
            if self.speed > 60:
                return f'Вы превышаете! Текущая скорость автомобиля: {self.speed}'
            return f'Текущая скорость автомобиля: {self.speed}'
        return 'Текущая скорость автомобиля: 0'

class WorkCar(Car):
    '''cлужебный автомобиль'''
    def show_speed(self):
        '''скорость для сл. авто'''
        if self.is_riding:
            if self.speed > 40:
                return f'Вы превышаете! Текущая скорость автомобиля: {self.speed}'
            return f'Текущая скорость автомобиля: {self.speed}'
        return 'Текущая скорость автомобиля: 0'

class SportCar(Car):
    '''Спортивный автомобиль'''

class PoliceCar(Car):
    '''Полицейский автомобиль'''
    is_police = True
    def __init__(self, name, speed, color = 'special-police'):
        super().__init__(name, speed, color)
        self.color = 'special-police'


town_car = TownCar('Peugeot', 90)
work_car = WorkCar('Renault', 50)
police_car = PoliceCar('BMW', 240)
sport_car = SportCar('Ferrari', 320, 'red')
print(
    f'Городской автомобиль, название: {town_car.name} \n '
    f'Скорость: {town_car.speed}, цвет: {town_car.color} \n '
    f'Рабочий автомобиль, название: {work_car.name} \n '
    f'Скорость: {work_car.speed}, цвет: {work_car.color} \n '
    f'Cпортивный автомобиль, название: {sport_car.name} \n '
    f'Скорость: {sport_car.speed}, цвет: {sport_car.color} \n '
    f'Полицейский автомобиль, название: {police_car.name} \n '
    f'Скорость: {police_car.speed}, цвет: {police_car.color} \n '
    f'Запускаем автомобили \n'
)
town_car.go()
work_car.go()
sport_car.go()
police_car.go()
print(
    f'Засекаем скорость: \n'
    f'Городской автомобиль: {town_car.show_speed()} \n '
    f'Рабочий автомобиль: {work_car.show_speed()} \n '
    f'Спортивный автомобиль: {sport_car.show_speed()} \n '
    f'Полицейский автомобиль: {police_car.show_speed()} \n '
    f'Остановим автомобили: \n '
)
town_car.stop()
work_car.stop()
sport_car.stop()
police_car.stop()
print(
    f'Засекаем остановленных авто: \n'
    f'Городской автомобиль: {town_car.show_speed()} \n '
    f'Рабочий автомобиль: {work_car.show_speed()} \n '
    f'Спортивный автомобиль: {sport_car.show_speed()} \n '
    f'Полицейский автомобиль: {police_car.show_speed()} \n '
)
