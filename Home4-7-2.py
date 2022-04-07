# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 09:23:30 2022

@author: z2- soft developer
"""

# Task7

def factor(x: int):
    a = 1
    if x <= 0:
        yield a
        
    for i in range(1, x + 1):
        a *= i
        yield a


for k in factor(6):
    print(k)
