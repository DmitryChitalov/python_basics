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

start_number = int(input('Enter the start number: '))
end_number = int(input('Enter the end number: '))

for elem in count(start_number):
    if elem >= end_number:
        break
    print(elem, end=' ')
print()

input_list = input('Enter the input list (divide by space): ').split()
repeats = int(input('Enter the number of repeats : '))

iteration = 0
for elem in cycle(input_list):
    iteration += 1
    if iteration > repeats:
        break
    print(elem, end=' ')
print()
