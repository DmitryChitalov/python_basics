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
from itertools import cycle

def my_count_func(start_number, stop_number):
    '''итератор от одного заданного числа до другого заданного числа'''
    for element in count(start_number):
        if element > stop_number:
            break
        print(element)

def my_cycle_func(lst, itr):
    '''итератор элементов списка'''
    counter = 1
    for element in cycle(lst):
        if counter > itr:
            break
        print(element)
        counter += 1

my_count_func(start_number = int(input("Введите начальное число: ")), stop_number = int(input("Введите конечное число: ")))
my_cycle_func(lst ="ABC", itr = int(input("Укажите нужное количество итераций: ")))
