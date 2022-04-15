# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 04:31:08 2022

@author: z2- soft developer
"""

# Task6

subjects = {}

with open('test1', encoding='utf-8') as f:
    for row in f:
        subjects_info = row.split()
        name = subjects_info[0].rstrip(':')

        subjects[name] = subjects_info[1:]
        
result = {}

for key, value in subjects.items():

    result[key] = sum(
        [
            int(hs[:hs.index('(')])
            for hs in value
            if hs != '—'
        ]
    )

print(result)
