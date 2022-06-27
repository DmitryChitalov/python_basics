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

# итератор A
print("*" * 10, "Iterator A")
START_ITERATOR = 1

for el in count(START_ITERATOR):
    if el > 10:
        break

    print(el)

# итератор B
print("*" * 10, "Iterator B")
cycling_list = [2, 5, 8, 3]
MAX_ITERATIONS = 16
ITERATION_COUNT = 0

for el in cycle(cycling_list):
    print(el)
    ITERATION_COUNT += 1

    if ITERATION_COUNT >= MAX_ITERATIONS:
        break
