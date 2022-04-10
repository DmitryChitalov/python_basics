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
from itertools import cycle, count

start_point = int(input('Start Numbers: '))
stop_point = start_point * 2 + 10 + 1

## a:
for i in count(start_point):
    if i < stop_point:
        print(i)
    else:
        break
del i



## b:
new_list = [i for i in range(stop_point)]
n_count = 0
for b in cycle(new_list):
    if n_count < stop_point + 10:
        print(b)
        n_count += 1
    else:
        break