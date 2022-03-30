# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 07:13:06 2022

@author: z2- soft developer
"""

# FOURTH TASK

user_number = input("Enter your number:\n")

list1 = []
for i in user_number:
    list1.append(i)
print(list1)
print(f"Your max figure in a number is\n{max(list1)}")
