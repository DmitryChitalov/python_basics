# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 03:44:21 2022

@author: z2- soft developer
"""

# Task2

my_file = open('a1file', 'r')


count = 0

for i in my_file:
    i = i.strip()
    words = i.split()
    number_of_words = len(words)
    count += 1
    print(f"{count} line is \n{i}")
    print(f"{number_of_words} words are at {count} line")
    # print(count)
print(f"General amount of lines - {count}")

my_file.close()
