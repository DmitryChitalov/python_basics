# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 07:14:24 2022

@author: z2- soft developer
"""

# SIXTH TASK

a = 2
b = 10
day_count = 1
while a <= b:
    print(f"At {day_count} day you achieved {round(a, 2)} km")
    day_count += 1
    day_increase = round(a * 0.1, 2)
    a += day_increase
print(f"At {day_count} day your result is {a} km")
