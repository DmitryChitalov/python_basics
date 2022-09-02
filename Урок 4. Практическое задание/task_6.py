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


def iter_int(n_st, n_end):
    iter_list = []
    for num in count(n_st):
        if num > n_end:
            break
        iter_list.append(num)
    return iter_list


def c_list(u_list):
    cnt = 1
    pos = 0
    for pos in cycle(u_list):
        if cnt >= len(u_list):
            break
        print(pos)
        cnt += 1
    yield pos


num_st = int(input(f"Введите число начала итерации: "))
num_en = int(input(f"Введите число окончания итерации: "))
print(f"Наш список: {iter_int(num_st, num_en)}")
print(f"Повтор списка: ")
for ex in c_list(iter_int(num_st, num_en)):
    print(ex)
