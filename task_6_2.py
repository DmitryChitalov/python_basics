"""Часть 2"""

from itertools import cycle

my_list = [1, 2, 3, 4, 5]
counter = 0

for elem in cycle(my_list):

    if counter > 10:
        break
    
    print(elem)
    counter += 1