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
     # atributes
     def __init__(self, speed, color, name, is_police):
         self.speed = speed
         self.color = color
         self.name = name
         self.is_police = is_police

     # methods
     def go(self):
         return f'{self.name} is started'

     def stop(self):
         return f'{self.name} is stopped'

     def turn_right(self):
         return f'{self.name} is turned right'

     def turn_left(self):
         return f'{self.name} is turned left'

     def show_speed(self):
         return f'Current speed {self.name} is {self.speed}'


 class TownCar(Car):
     def __init__(self, speed, color, name, is_police):
         super().__init__(speed, color, name, is_police)

     def show_speed(self):
         print(f'Current speed of town car {self.name} is {self.speed}')

         if self.speed > 40:
             return f'Speed of {self.name} is higher than allow for town car'
         else:
             return f'Speed of {self.name} is normal for town car'

 class SportCar(Car):
     def __init__(self, speed, color, name, is_police):
         super().__init__(speed, color, name, is_police)


 class WorkCar(Car):
     def __init__(self, speed, color, name, is_police):
         super().__init__(speed, color, name, is_police)

     def show_speed(self):
         print(f'Current speed of work car {self.name} is {self.speed}')

         if self.speed > 60:
             return f'Speed of {self.name} is higher than allow for work car'


 class PoliceCar(Car):
     def __init__(self, speed, color, name, is_police):
         super().__init__(speed, color, name, is_police)

     def police(self):
         if self.is_police:
             return f'{self.name} is from police department'
         else:
             return f'{self.name} is not from police department'


 audi = SportCar(100, 'Red', 'Audi', False)
 oka = TownCar(30, 'White', 'Oka', False)
 lada = WorkCar(70, 'Rose', 'Lada', True)
 ford = PoliceCar(110, 'Blue',  'Ford', True)
 print(lada.turn_left())
 print(f'When {oka.turn_right()}, then {audi.stop()}')
 print(f'{lada.go()} with speed exactly {lada.show_speed()}')
 print(f'{lada.name} is {lada.color}')
 print(f'Is {audi.name} a police car? {audi.is_police}')
 print(f'Is {lada.name}  a police car? {lada.is_police}')
 print(audi.show_speed())
 print(oka.show_speed())
 print(ford.police())
 print(ford.show_speed())
