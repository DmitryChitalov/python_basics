# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 03:56:15 2022

@author: z2- soft developer
"""

# Task5

class Stationery:
    title: str

    def draw(self):
        print("The drawing starts!")


class Pen(Stationery):
    def draw(self):
        print("The Pen is working!")


class Pencil(Stationery):
    def draw(self):
        print("The Pencil is working!")


class Handle(Stationery):
    def draw(self):
        print("Now the marker starts!")


test1 = Stationery()
test2 = Pen()
test3 = Pencil()
test4 = Handle()
test1.draw()
test2.draw()
test3.draw()
test4.draw()
