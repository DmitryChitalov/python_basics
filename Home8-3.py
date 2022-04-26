# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 14:30:55 2022

@author: z2- soft developer
"""

# Task3

class NotaNumListMistake(Exception):
    pass


numbers = []


def append_number(number_list: list):
    value = input("Enter a number:\n")

    try:
        number_list.append(float(value))
    except ValueError:
        raise NotaNumListMistake(f"You entered '{value}' instead of a number")


while True:
    try:
        append_number(numbers)
    except NotaNumListMistake as exception:
        print(exception)
    except KeyboardInterrupt:
        print(f"\nNumber list is {numbers}")
        break
