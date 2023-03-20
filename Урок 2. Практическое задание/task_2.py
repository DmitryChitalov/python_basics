"""
Задание 2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""

task_numbers = input("Введите целые числа через пробел: ")
task_list = task_numbers.split(' ')
list_elements = len(task_list)
result_list = list()

if list_elements % 2 != 0:
    list_elements -= 1
    result_list.append(task_list[list_elements])
while list_elements != 0:
    b = [task_list[list_elements-2], task_list[list_elements-1]]
    result_list.extend(b)
    list_elements -= 2
result_list.reverse()
print(f"Результат: {result_list}")
