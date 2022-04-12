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
import string_extension

#Вариант 1 без itertools
def next_number(first, last):
    while first <= last:
        yield first
        first += 1


def replicate_list_element(lst, replication_count):
    iterator = 0
    ndx = 0
    lst_len = len(lst)
    replication_count = replication_count
    while iterator < replication_count and lst_len > 0:
        if ndx >= lst_len:
            ndx = 0
        
        yield lst[ndx]
        ndx += 1
        iterator += 1

#Вариант 2 с itertools
def next_number_itertools(first, last):
    for el in count(first):
        if el <= last:
            yield el
        else:
            break


def replicate_list_element_itertools(lst, replication_count):
    replication_count = replication_count
    for ndx, el in enumerate(cycle(lst)):
        if ndx < replication_count:
            yield el
        else:
            break

input_str = input("Please, inpur first integer number: ")

if string_extension.is_int(input_str):
    first_number = int(input_str)
    last_number = abs(first_number) * 3

    print(f"V1: {[el for el in next_number(first_number, last_number)]}")

    print(f"V2: {[el for el in next_number_itertools(first_number, last_number)]}")
else:
    print("Error: your input value is not a integer number")




input_list = input("Please, input any elements separated by space: ").split(" ")
input_replication_count = input("Please, input replication count as integer number: ")

if string_extension.is_int(input_replication_count):
    replication_count = int(input_replication_count)


    print(f"V1: {[el for el in replicate_list_element(input_list, replication_count)]}")
    print(f"V2: {[el for el in replicate_list_element_itertools(input_list, replication_count)]}")
else:
    print("Error: your input value is not a integer number")

counter = count()