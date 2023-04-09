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

from argparse import ArgumentParser
from itertools import count, cycle
from time import sleep

parser = ArgumentParser()
parser.add_argument('--count', type=int, default=7)
parser.add_argument('--cycle', type=int, default=10)
args = parser.parse_args()
for el in count(args.count):
    if el > args.count + 7:
        break
    else:
        print(el)
        sleep(1)

m = 0
for el in cycle(['Hi', 'Hello']):
    if m > args.cycle:
        break
    print(el)
    sleep(1)
    m += 1
