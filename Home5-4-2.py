# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 13:49:35 2022

@author: z2- soft developer
"""

# Task4

replacements = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}

with open('a', encoding='utf-8') as infile, open('anew', 'w', encoding='utf-8') as outfile:
    for line in infile:
        for src, target in replacements.items():
            line = line.replace(src, target)
        outfile.write(line)
        print(line)
