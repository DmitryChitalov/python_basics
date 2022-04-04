# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 23:47:36 2022

@author: z2- soft developer
"""

# Fifth Task

total = 0

while True:
    user_numbers = input("Enter a string of numbers using a space: \n").split()
    is_sp_character = False

    for n in user_numbers:
        if n.isdigit():
            total += int(n)
        else:
            is_sp_character = True
            break

    print(f"General amount of numbers = {total}")

    if is_sp_character:
        break
