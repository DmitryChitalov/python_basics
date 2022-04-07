# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:17:53 2022

@author: z2- soft developer
"""

from itertools import count, cycle

print("--" * 20, "iterator")
start_iterator = 7

for i in count(start_iterator):
    if i > 10:
        break
    print(i)
    
print("##" * 20, "iterator")
cycling_list = [4, 9, 3, 33, 23, 55]
max_iterations = 12
iteration_count = 0

for i in cycle(cycling_list):
    print(i)
    iteration_count += 1
    
    if iteration_count >= max_iterations:
        break
