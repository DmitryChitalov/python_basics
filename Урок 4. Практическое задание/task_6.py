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


def int_num(f_num):
    rez = []
    for i in count(f_num):
        if i > 100:
            break
        else:
            rez.append(i)
    return rez


n = int(input('Введите начало : '))
print(int_num(n))


def copy_lst(my_list, next_r):
    rez = []
    my_count = 0
    for i in cycle(my_list):
        if my_count > next_r - 1:
            break
        rez.append(i)
        my_count += 1
    return rez


temp_list = ['asd', 'qwe', 'zxc', 'qaz']
k = int(input('Введите количество повторений : '))
print(copy_lst(temp_list, k))
