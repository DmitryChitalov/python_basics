# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 03:26:14 2022

@author: z2- soft developer
"""

# Task5

my_list = [9, 7, 7, 5, 5, 4, 3]
user_rate = int(input("Enter your rate for a project:\n"))
my_list.append(user_rate)
my_list.sort(reverse=True)
print(my_list)
