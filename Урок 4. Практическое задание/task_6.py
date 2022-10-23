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

from itertools import count
from itertools import cycle
from itertools import takewhile

list1 = list(takewhile(lambda i: i < 50, count(5, 3)))
print(list1)

cyc_list = [3, 4, 7, 1]
list2 = []
amt = 0
for el in cycle(cyc_list):
    if amt + el > 50:
        break
    amt += el
    list2.append(el)

print(f"amount of {list2} = {amt}")
