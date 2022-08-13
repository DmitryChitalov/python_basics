"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""

from sys import argv
from itertools import cycle, count

count_list = []
for el in count(3):
    if el > 10:
        break
    else:
        if el % 2 == 0:
            count_list.append(el)

cycle_list = []
cycle_string = "ABC"
cycle_iter_count = 0

for el in cycle(cycle_string):
    if cycle_iter_count > 10:
        break
    else:
        cycle_list.append(el)
    cycle_iter_count += 1

print(f"Count(): {count_list}")
print(f"Cycle(): {cycle_list}")
"""
Count(): [4, 6, 8, 10]
Cycle(): ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B']
"""
