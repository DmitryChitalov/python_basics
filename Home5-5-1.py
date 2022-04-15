# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 14:46:25 2022

@author: z2- soft developer
"""

# Task5

total = 0

with open('numbers', 'w+') as ws:
    ws.write(input("Enter your numbers using space you want to sum: \n"))
with open('numbers', 'r+') as rs:
    is_a_sp = False
    n = rs.read().split()
    for i in n:
        if i.isdigit():
            total += int(i)
        else:
            is_a_sp = True
            break
print(f"Sum of user numbers is \n{total}")
if is_a_sp:
    exit()
