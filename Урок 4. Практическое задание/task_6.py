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

start = int(input("Введите число с какого начнется генерация: "))
stop = int(input("Введите число до какого генерировать: "))
count_num = 0
my_list = []
for i in count(count_num):
    if i > stop:
        break
    else:
        my_list.append(i)
        
for i in cycle(my_list):
    if count_num > stop:
        break
    print(i)
    count_num += 1
