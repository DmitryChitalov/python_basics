# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 03:53:27 2022

@author: z2- soft developer
"""

# Task5

from random import randrange

random_numbers = [randrange(1, 200) for _ in range(50)]

with open('test1', 'w') as output_data:
    output_data.write(" ".join(map(str, random_numbers)))

with open('test1') as input_data:
    numbers = input_data.read().split()

    print(
        sum(float(x) for x in numbers)
    )
