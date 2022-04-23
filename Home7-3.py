# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 10:14:55 2022

@author: z2- soft developer
"""

# Task3

class Cell:
    __count: int

    def __init__(self, count: int):
        assert count > 0, "Quantity of cells have to be more than 0"
        self.__count = count

    def __add__(self, other: 'Cell'):
        self.validate_item(other)
        value = self.count + other.count
        return Cell(value)

    def __sub__(self, other: 'Cell'):
        self.validate_item(other)
        value = self.count - other.count
        assert  value > 0, "The difference less than 0"
        return Cell(value)

    def __mul__(self, other: 'Cell'):
        self.validate_item(other)
        value = self.count * other.count
        return Cell(value)

    def __truediv__(self, other: 'Cell'):
        self.validate_item(other)
        value = round(self.count / self.count)
        return Cell(value)

    def __str__(self):
        return str(self.__count)

    def validate_item(self, other):
        assert isinstance(other, self.__class__), "Actions are only possible for cells "

    @property
    def count(self) -> int:
        return self.__count

    @staticmethod
    def mk_order(cell_object: 'Cell', count_per_row: int) -> str:
        items = '*' * cell_object.count
        chunks = [
            items[idx:idx + count_per_row]
            for idx in range(0, len(items), count_per_row)
        ]

        return '\n'.join(chunks)


atest = Cell(55)
btest = Cell(23)
ctest = Cell(11)

print(atest + btest)
print(atest - btest)
print(atest * btest)
print(atest / btest)

print(Cell.mk_order(ctest, 7))
