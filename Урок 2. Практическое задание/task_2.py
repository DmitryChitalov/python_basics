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

numbers = input("Введите целые числа через пробел: ")


list_of_numbers = numbers.split(' ')


for el in range(0, (len(list_of_numbers) - len(list_of_numbers) % 2), 2):
    list_of_numbers[el], list_of_numbers[el + 1] = list_of_numbers[el + 1], list_of_numbers[el]
    # tmp = list_of_numbers[el]
    # list_of_numbers[el] = list_of_numbers[el + 1]
    # list_of_numbers[el + 1] = tmp
print(list_of_numbers)
