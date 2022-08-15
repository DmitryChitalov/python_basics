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

from number_generator import get_number, get_number_repeating

while True:
    start_gen = input("Введите начальный диапазон генерации списка: ")
    try:
        start_gen = int(start_gen)
        break
    except ValueError:
        print("Введите целое положительное число")
        continue

while True:
    end_gen = input("Введите конечный диапазон генерации списка: ")
    try:
        end_gen = int(end_gen)
        break
    except ValueError:
        print("Введите целое положительное число")
        continue

print(get_number(start_gen, end_gen))

lst_gen = [int(el) for el in input("Введите числа через пробел для генерации повторяющегося списка: ").split(" ")]

while True:
    end_gen = input("Введите конечный диапазон генерации повторяющегося списка: ")
    try:
        end_gen = int(end_gen)
        break
    except ValueError:
        print("Введите целое положительное число")
        continue

print(get_number_repeating(lst_gen, end_gen))
