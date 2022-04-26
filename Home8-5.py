# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 14:46:59 2022

@author: z2- soft developer
"""

# Task5

class ComplexNumber:
    real: float
    indeterminate: float

    def __init__(self, real: float, indeterminate: float):
        self.real = real
        self.indeterminate = indeterminate

    def __add__(self, other: 'ComplexNumber'):
        return ComplexNumber(
            self.real + other.real,
            self.indeterminate + other.indeterminate
        )

    def __mul__(self, other: 'ComplexNumber'):
        r1 = self.real * other.real
        r2 = self.indeterminate * other.indeterminate * -1

        i1 = self.real * other.indeterminate
        i2 = self.indeterminate * other.real

        real = r1 + r2
        indeterminate = i1 + i2

        return ComplexNumber(real, indeterminate)

    def __str__(self):
        return f"({self.real}{'+' if self.indeterminate > 0 else ''}{self.indeterminate}i)"


a = ComplexNumber(4, 55)
b = ComplexNumber(6, 99)

print(a + b)

print(a * b)
