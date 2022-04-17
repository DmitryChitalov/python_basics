# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 01:19:20 2022

@author: z2- soft developer
"""

# Task1

from time import sleep


class TrafficLight:
    __color1: str
    __color2: str
    __color3: str

    def __init__(self, color1='Red', color2='Yellow', color3='Green'):   # constructor
        self.__color1 = color1
        self.__color2 = color2
        self.__color3 = color3

    def running(self):
        while True:                     # eternal cycle
            print(self.__color1)
            sleep(7)
            print(self.__color2)
            sleep(2)
            print(self.__color3)
            sleep(15)


semaphore = TrafficLight()
semaphore.running()
