# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 09:38:41 2022

@author: z2- soft developer
"""

# Task3

salaries = []
with open("a1file", "r") as fs:
    for i in fs:
        content = i.split()
        salaries.append(float(content[1]))
        if float(content[1]) < 20000:
            print(content)
avg = sum(salaries)/len(salaries)
print(f"List of salaries \n {salaries}")
print(f"General amount of salaries \n {sum(salaries)}")
print(f"Quantity of salaries lines \n {len(salaries)}")
print(f"The average sum of salaries \n {avg}")
