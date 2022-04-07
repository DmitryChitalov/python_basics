# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 05:41:11 2022

@author: z2- soft developer
"""

# Task2

list1 = [200, 3, 15, 45, 2, 2, 5, 11, 8, 2, 88, 125, 55]
list2 = [
    val for i, val in enumerate(list1) if i > 0 and list1[i - 1] < val
    ]

print(list2)
