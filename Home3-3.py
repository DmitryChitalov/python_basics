# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 02:29:57 2022

@author: z2- soft developer
"""

# Third Task


def my_func(*args):
    max2, max1 = sorted(args)[-2:]

    return max1 + max2


result = my_func(99, 11, 55)
print(result)
