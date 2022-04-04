# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 02:53:40 2022

@author: z2- soft developer
"""

# Task3

month_number = int(input("Enter the number of a month:\n"))

m_season = {
    "зима": (12, 1, 2),
    "весна": (3, 4, 5),
    "лето": (6, 7, 8),
    "осень": (9, 10, 11),
    }
for season, number in m_season.items():
    if month_number in number:
        print(f"{season}")
        
