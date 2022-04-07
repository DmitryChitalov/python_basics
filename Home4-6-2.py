# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 08:24:13 2022

@author: z2- soft developer
"""


# Task6

from itertools import cycle

list1 = [33, 88, 1, 0, 'd', b'c', 55.234]
n = 0
for i in cycle(list1):
    print(end=f"{n}- {i} \n")
    n += 1
    if n > 11:
        break
