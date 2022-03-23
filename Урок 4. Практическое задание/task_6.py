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


def count_func(start_num, stop_num):
    for num in count(start_num):
        if num > stop_num:
            break
        else:
            print(num)


def cycle_func(number_list, iteration):
    i = 0
    iterator = cycle(number_list)
    while i < iteration:
        print(next(iterator))
        i += 1


count_func(start_num=int(input('Enter start number: ')),
           stop_num=int(input('Enter finish number: ')))
cycle_func(number_list=[1, 2, 3], iteration=int(input('Enter cycle number ')))
