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
#!/usr/bin/env python3
import random
import itertools

magic_numbers = [1, 2]
script_choice = 0
predetermined_list = []

for i in range(0, 6):
    x = random.randint(0, 666)
    predetermined_list.append(x)

while script_choice not in magic_numbers:
    script_choice = int(input("Какой 'небольшой скрипт' желаете выполнить-с, первый-с (1) или второй-с (2)?: "))

if script_choice == 1:
    print(f"Отличный выбор. Питон вам предложит итератор, генерирующий целые числа, начиная с указанного.")
    starting_point = int(input("Введите число: "))
else:
    print(f"Отличный выбор. Питон вам предложит итератор, повторяющий элементы некоторого списка, определенного заранее (Леонид Якубович подмигивает).")
    print(f"Список в студию! {predetermined_list}.")

from itertools import count, cycle

list_int = []

a = int(input("Первое в последовательности >>> "))
n = int(input("Последнее в последовательности >>> "))

for x in count(a):
    if x > n:
        break
    print(x)
    list_int.append(x)

print()
print(list_int)

count = 0
for item in cycle(list_int):
    if count >= len(list_int):
        break
    print(item)
    count += 1
