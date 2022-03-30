# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 07:13:52 2022

@author: z2- soft developer
"""

# FIFTH TASK

proceeds = int(input("What is your firm-corporation' proceeds?\n"))
expenses = int(input("What is your firm' expenses?\n"))
employee_number = int(input("How many employees do your firm have?\n"))
income = proceeds - expenses
income_for_person = round(income/employee_number, 2)
if proceeds > expenses:
    print("You are doing very well!!! You have income!!!")
    profitability = round(income/proceeds, 2)
    print(f"Your profitability is \n{profitability}")
    print(f"Your income for an employee is \n{income_for_person}")
else:
    print("You need work over optimization!!!")
