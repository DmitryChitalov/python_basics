# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 09:50:54 2022

@author: z2- soft developer
"""

# Task1

class Matrix:
    value: list

    def __init__(self, value: list):
        self.value = value

    def __add__(self, other: 'Matrix'):
        try:
            rows_count = len(self.value)
            items_count = len(self.value[0])

            new_value = [
                [
                    self.value[row][idx] + other.value[row][idx]
                    for idx in range(items_count)
                ]
                for row in range(rows_count)
            ]

            return Matrix(new_value)
        except IndexError:
            print("Mistake - here are the matrices of different size")
            exit(1)

    def __str__(self):
        return "\n".join(
            str(row).strip('[]').replace(',', '')
            for row in self.value
        )


a = Matrix([[31, 22], [37, 43], [51, 86]])
b = Matrix([[83, 66], [29, 38], [19, 93]])

result = a + b

print(result)
