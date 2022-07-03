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

print(f"а) итератор, генерирующий целые числа, начиная с указанного")

num_list = []

num = int(input("Введите число: "))

for x in count(num):
    if x > num + 9:
        break
    print(x)
    num_list.append(x)

print(f"б) итератор, повторяющий элементы некоторого списка, определенного заранее")

count = 0
for b in cycle(num_list):
    if count >= len(num_list):
        break
    print(b)
    count += 1

