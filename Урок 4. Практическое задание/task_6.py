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


def iterator(start_number):
    new_list = []
    for x in count(start_number):
        if x > start_number + 15:
            break
        else:
            new_list.append(str(x))
    return new_list


def understudy_iterator(inner_list=[]):
    new_list = []
    i = cycle(inner_list)
    for x in range(len(inner_list)):
        new_list.append(next(i))
    return new_list


iterator_list = iterator(13)

print(iterator_list)
print(understudy_iterator(iterator_list))
