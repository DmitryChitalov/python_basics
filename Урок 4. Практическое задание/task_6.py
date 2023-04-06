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

# Итератор, генерирующий целые числа, начиная с указанного
def generate_numbers(start, end):
    for number in count(start):
        if number > end:
            break
        yield number

from itertools import count, cycle

# Итератор, генерирующий целые числа, начиная с указанного
def generator(start, stop):
    for num in count(start):
        if num > stop:
            break
        yield num


def repeater(data, max_repeats):
    for item in cycle(data):
        if max_repeats == 0:
            break
        yield item
        max_repeats -= 1


for num in generator(3, 10):
    print(num)

my_list = ["a", "b", "c"]
for item in repeater(my_list, 3):
    print(item)
