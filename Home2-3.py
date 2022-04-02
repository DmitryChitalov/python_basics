# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 02:53:40 2022

@author: z2- soft developer
"""

# Task3

seasons = ["winter", "spring", "summer", "autumn_fall"]
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn_fall = [9, 10, 11]
month_number = int(input("Enter the number of a month:\n"))
for i in winter:
    if month_number == winter[0] or month_number == winter[1] or month_number == winter[2]:
        print(f"You chose the {seasons[0]} month!")
        break
    if month_number == spring[0] or month_number == spring[1] or month_number == spring[2]:
        print(f"You chose the {seasons[1]} month!")
        break
    if month_number == summer[0] or month_number == summer[1] or month_number == summer[2]:
        print(f"You chose the {seasons[2]} month!")
        break
    if month_number == autumn_fall[0] or month_number == autumn_fall[1] or month_number == autumn_fall[2]:
        print(f"You chose the {seasons[3]} month!")
        break

m_season = {
    "зима": (12, 1, 2),
    "весна": (3, 4, 5),
    "лето": (6, 7, 8),
    "осень": (9, 10, 11),
    }
for season, number in m_season.items():
    if month_number in number:
        print(f"{season}")
        