# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 03:06:08 2022

@author: z2- soft developer
"""

# Task3

class Worker:
    name: str
    surname: str
    position: str
    _income: dict
    
    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


client1 = Position("Serge", "Mogov", "engineer", 7234, 444)
print(client1.get_full_name(), client1.get_total_income())
