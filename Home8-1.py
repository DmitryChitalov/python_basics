# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 14:04:00 2022

@author: z2- soft developer
"""

# Task1

class Date:
    day: int
    month: int
    year: int

    def __init__(self, date_string: str):
        numbers = Date.extract_numbers(date_string)
        self.validate_numbers(numbers)

        self.day, self.month, self.year = numbers

    @classmethod
    def extract_numbers(cls, date_string: str) -> list:
        return [int(x) for x in date_string.split('-')]

    @staticmethod
    def validate_numbers(numbers: list):
        d, m, y = numbers

        assert 1 <= d <= 31, "Wrong date!!!"
        assert 1 <= m <= 12, "Wrong month!!!"
        assert 1929 <= y <= 2023, "Wrong year!!!"


my_date = Date('22-12-1544')
