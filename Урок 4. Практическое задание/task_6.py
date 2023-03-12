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

def generate_numbers_between(start, end):
    res = []
    for n in count(start):
        if n > end:
            break
        res.append(n)
    return res

def repeat_numbers(list, max_count):
    res = []
    count = 0
    for n in cycle(list):
        count = count + 1
        if count > max_count:
            break
        res.append(n)
    return res

start_number = int(input("Введите число, с которого начать:"))
end_number = int(input("Введите число, на котором нужно остановиться:"))
max_count_number = int(input("Введите максимальное количество для 2го списка:"))
list = generate_numbers_between(start_number, end_number)
print("1й цикл:", list)
print("2й цикл:", repeat_numbers(list, max_count_number))
