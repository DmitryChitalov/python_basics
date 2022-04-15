# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 02:04:48 2022

@author: z2- soft developer
"""

# Task1

mk_file = open('a1file', 'w')

if mk_file.writable():
    strings = input('Enter data: \n')
    b = strings.split()

    for x in b:
        print(x, file=mk_file)
else:
    print('Impossible!!!')

mk_file.close()
