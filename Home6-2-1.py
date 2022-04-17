# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 01:55:01 2022

@author: z2- soft developer
"""

# Task2

class Road:
    _length: float
    _width: float

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_measuring(self):
        mass_for_onesqm = 25
        thickness = 5
        total_asph = self._length * self._width * mass_for_onesqm * thickness
        print(f"Total amount of asphalt is {self._length} * {self._width} * {mass_for_onesqm} * {thickness} = {total_asph / 1000}  t")


test1 = Road(20, 5000)
test1.asphalt_measuring()
