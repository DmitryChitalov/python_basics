# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 08:22:42 2022

@author: z2- soft developer
"""

# Task6

from itertools import count

for x in count(3, 1):
    if x > 10:
        break

    print(x)
