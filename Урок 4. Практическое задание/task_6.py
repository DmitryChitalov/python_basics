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
import itertools


def iter_one(n=3, end=10):
    array = []
    data = itertools.count(start=n, step=1)
    for i in data:
        if i >= end:
            break
        array.append(i)
    return array


def iter_two(elements=10):
    array = [1, 23, 45, 5, 67, 78, 4]
    res_array = []
    for i in itertools.cycle(array):
        if len(res_array) > elements:
            break
        res_array.append(i)
    return res_array


print(iter_one())
print(iter_two())
