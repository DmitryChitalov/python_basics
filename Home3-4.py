# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 03:26:59 2022

@author: z2- soft developer
"""

# Fourth Task

def my_func(x, y):
    return x ** abs(y)


result = my_func(5, -4)
print(result)


def my_func1(x, y):
    a = x
    for i in range(abs(y)-1):
        a *= x
        print(a)
    return a


result1 = my_func1(8, -5)
print(result1)
