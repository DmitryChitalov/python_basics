# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 14:19:41 2022

@author: z2- soft developer
"""

# Task2

class CustomZeroMistake(Exception):
    pass


def get_numerator() -> int:
    return int(input("Введите числитель:\n"))


def get_denominator() -> int:
    value = int(input("Введите знаменатель:\n"))

    if value == 0:
        raise CustomZeroMistake

    return value


while True:
    try:
        numerator = get_numerator()
        denominator = get_denominator()

        print(f"Result = {numerator / denominator}")
    except CustomZeroMistake:
        print("Нельзя вводить 0!!!")
    except KeyboardInterrupt:
        break
