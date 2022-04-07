# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 07:37:16 2022

@author: z2- soft developer
"""

# Task5

from functools import reduce

list1 = [i for i in range(100, 1001) if i % 2 == 0]
print(list1)

get_multiplication = reduce(lambda x, y: x * y, list1, 1)

print(get_multiplication)
