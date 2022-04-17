# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 06:33:18 2022

@author: z2- soft developer
"""

# Task4


class Car:
    speed: int
    color: str
    name: str
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str) -> None:
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f"{self.name}: start")

    def stop(self):
        print(f"{self.name}: stop")

    def turn(self, direction: str):
        print(f"{self.name}: turning - {direction}")

    def show_speed(self):
        print(f"{self.name}: speed = {self.speed} km/h")


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"{self.name}: speeding violation- excessive speed!!!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"{self.name}: excessive speed- speeding violation!!!")


class PoliceCar(Car):
    is_police: bool = True


cars = [
    SportCar(360, "green", "Toyota"),
    TownCar(220, "orange", "Niva"),
    WorkCar(180, "violet", "BMW"),
    PoliceCar(550, "grey", "Mercedes")
]

cars[0].go()
cars[1].turn("to the left")
cars[2].stop()

for car in cars:
    car.show_speed()
