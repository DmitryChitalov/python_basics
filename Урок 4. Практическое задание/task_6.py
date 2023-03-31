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
first_number = int(input())
second_number = int(input())

for el in count(first_number):
    if el >= second_number:
        break
        print(el, end='')
    print()

input_list = input().split()
repeats = int(input())

iteration = 0
for el in cycle(input_list):
    iteration += 1
    if iteration > repeats:
        break
    print(el, end=' ')


