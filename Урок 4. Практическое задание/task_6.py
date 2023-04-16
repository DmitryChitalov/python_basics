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


def integer_generator(start_number, end_number):
    out_list = []
    for el in count(start_number):
        if el > end_number:
            break
        out_list.append(el)
    return out_list


def repeating_elements(input_list, counter):
    ex = 1
    out_list = []
    for i in cycle(input_list):
        if ex > counter:
            break
        ex += 1
        out_list.append(i)
    return out_list


if __name__ == "__main__":
    my_list = integer_generator(3, 10)
    print(my_list)
    print(repeating_elements(my_list, 10))
