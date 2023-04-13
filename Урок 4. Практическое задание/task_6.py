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


def use_count(start, stop):
    counter = count(start)
    for i in counter:
        print(i)
        if i >= stop:
            break


def use_cycle(lst, repeat_list_times):
    cycler = cycle(lst)
    counter = 0
    while True:
        print(next(cycler))
        counter += 1
        if counter >= repeat_list_times * len(lst):
            break


use_count(3, 10)
use_cycle(range(3), 3)
