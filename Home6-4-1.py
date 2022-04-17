# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 03:43:58 2022

@author: z2- soft developer
"""

# Task4

class Car:
    speed: float
    color: str
    name: str
    is_police: bool

    def go(self):
        print("The car is going")

    def stop(self):
        print("Stopped")

    def turn_right(self):
        print("Turned to the right")

    def turn_left(self):
        print("Turned to the left")

    def show_speed(self, current_speed):
        print(f"{current_speed}")


class TownCar(Car):
    def show_speed(self, current_speed):
        if current_speed > 60:
            print("The speed is dangerously great")


class SportCar(Car):
    print("It's a sportive car!")


class WorkCar(Car):
    def show_speed(self, current_speed):
        if current_speed > 40:
            print("The speed is dangerously great")


class PoliceCar(Car):
    is_police = True
    print("It's a police car!!!")


auto = Car()
auto1 = TownCar()
auto2 = SportCar()
auto3 = WorkCar()
auto4 = PoliceCar()
auto1.show_speed(55)
auto2.show_speed(77)
auto3.show_speed(88)
auto4.show_speed(22)
auto.go()
auto.turn_left()
auto.stop()
