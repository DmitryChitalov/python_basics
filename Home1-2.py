# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 07:06:32 2022

@author: z2- soft developer
"""

# SECOND TASK

time_In_secs = int(input("Enter the time for your project in seconds:\n"))
hours_in_data = time_In_secs // 3600
minutes_in_data = (time_In_secs % 3600) // 60
secs_in_data = (time_In_secs % 3600) % 60
print(f"Your time for project is {hours_in_data}:{minutes_in_data}:{secs_in_data}")
print("Your time for project is {}:{}:{}".format(hours_in_data, minutes_in_data, secs_in_data))
