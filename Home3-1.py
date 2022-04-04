# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 01:12:47 2022

@author: z2- soft developer
"""

# First Task

def mk_division(a, b):  # make a function for division
    try:
        return a/b
    except ZeroDivisionError:   # work over trying to divide by 0
        if b == 0:
            print("Zero!!!Error!!!")


c = int(input("Enter your first number: "))     # getting a user's input
d = int(input("Enter your second number: "))
result = mk_division(c, d)                      # getting a result
print(result)
