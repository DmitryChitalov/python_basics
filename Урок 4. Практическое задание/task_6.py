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

from itertools import count, cycle
from sys import argv

def iterator_range(begin, end):
    my_list = []
    for el in count(begin):
        if el > end:
            break
        else:
            print(el)
            my_list.append(el)
    return my_list


def iterator_cycle(input_list, end_of_cycle):
    my_list = []
    iterator = 1
    for el in cycle(input_list):
        if iterator > end_of_cycle:
            break
        print(el)
        my_list.append(el)
        iterator = iterator + 1
    return my_list

script_name, begin_range, end_range, end_cycle = argv
init_list = iterator_range(int(begin_range), int(end_range))
print()
iterator_cycle(init_list, int(end_cycle))
