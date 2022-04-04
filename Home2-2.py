# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 02:51:16 2022

@author: z2- soft developer
"""

# Task2

my_list = [55, "sky", 22.55, b's', 1, 10, "problem"]
m = len(my_list) - 1

for i in range(0, m, 2):
    next_i = i + 1
    my_list[i], my_list[next_i] = my_list[next_i], my_list[i]
print(my_list)
