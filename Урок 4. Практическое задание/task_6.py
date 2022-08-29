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


def even_number_generator(from_number):
    for el in count(from_number):
        if not el & 0x01:
            yield el


start = 8
stop = 100

for i in even_number_generator(start):
    print(i)
    if i >= stop:
        break

from itertools import cycle


def list_repeater_generator(src_list):
    for el in cycle(src_list):
        yield el


gen = list_repeater_generator(['1234', 'True', 'авс'])
for i in range(10):
    print(next(gen))
