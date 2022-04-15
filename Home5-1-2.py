# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 00:53:31 2022

@author: z2- soft developer
"""

# Task1

strings = []

while True:
    with open('test1', 'a+') as app_str:
        string = input("ВВедите строку: ")
        print(string)
        if not string:
            break

        app_str.write(f"{string}\n")
