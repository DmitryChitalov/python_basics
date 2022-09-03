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

# Выводим задание на экран
print(f'Реализовать два небольших скрипта:\n'
      f'а) итератор, генерирующий целые числа, начиная с указанного,\n'
      f'б) итератор, повторяющий элементы некоторого списка, определенного заранее.\n\n'
      f'Подсказка: использовать функцию count() и cycle() модуля itertools.\n'
      f'Обратите внимание, что создаваемый цикл не должен быть бесконечным.\n'
      f'Необходимо предусмотреть условие его завершения.\n')

# Определяем переменные
start_num = 3
finish_num = 10
index = 0
list_from_count = []
list_from_cycle = []
# Применяем count() для генерации списка
for el in count(start_num):
    if el > finish_num:
        break
    list_from_count.append(el)

# Применяем cycle() для генерации списка
for el in cycle(list_from_count):
    if index > finish_num + 5:
        break
    list_from_cycle.append(el)
    index = index + 1

# Выводим результат на экран
print(f'Сгенерированныйй при помощи count() список: {list_from_count}\n'
      f'Сгенерированныйй при помощи cycle() список: {list_from_cycle}')
