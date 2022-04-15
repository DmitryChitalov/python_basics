# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:47:28 2022

@author: z2- soft developer
"""

# Task2

with open('test1') as fs:
    rows = fs.readlines()
    expanded_rows = [row.split() for row in rows]

rows_count, words_count = len(rows), sum([len(word_list) for word_list in expanded_rows])

print(f"Всего строк - {rows_count}, всего слов - {words_count}")
