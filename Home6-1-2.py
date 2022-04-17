# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 05:05:50 2022

@author: z2- soft developer
"""

# Task1

import itertools
import time


class TrafficLight:
    __color: str
    __timing: dict

    def __init__(self, red_time: int = 7, yellow_time: int = 3, green_time: int = 15):
        self.__timing = {
            "red": red_time,
            "yellow": yellow_time,
            "green": green_time
        }

    def running(self):
        for mode, timer in itertools.cycle(self.__timing.items()):
            self.__color = mode

            for second in range(timer):
                print(f"{self} [{second + 1}]")
                time.sleep(1)

    def __repr__(self):
        return f"Current regime = {self.__color}"


try:
    traffic_light = TrafficLight(7, 3, 11)
    traffic_light.running()
except KeyboardInterrupt:
    print("Exit the program")

