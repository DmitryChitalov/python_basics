# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 02:24:58 2022

@author: z2- soft developer
"""

# Task3

with open('a1file') as fs:
    employee_list = [employee_line.split() for employee_line in fs.readlines()]

employee_with_info = [
    {'name': employee[0], 'salary': float(employee[1])}
    for employee in employee_list
    if len(employee) > 1
]

for employee in employee_with_info:
    if employee['salary'] < 20_000:
        print(employee['name'])

for employee in filter(lambda item: item['salary'] < 20_000, employee_with_info):
    print(employee['name'])
    