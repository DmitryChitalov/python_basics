# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 06:48:22 2022

@author: z2- soft developer
"""

# Task 5


class Stationery:
    title: str
    _message = "Start of drawing"

    def draw(self):
        print(self._message)


class Pen(Stationery):
    _message = "We draw with pen"


class Pencil(Stationery):
    _message = "We draw with pencil"


class Handle(Stationery):
    _message = "We draw with marker"


items = [Stationery(), Pen(), Pencil(), Handle()]

for item in items:
    item.draw()
    