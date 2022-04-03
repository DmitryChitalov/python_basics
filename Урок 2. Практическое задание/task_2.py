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

input_string = input("Please, input array of elements with delimiter as space: ")
input_array = input_string.split(" ")

index = 0
array_len = len(input_array)
while index < array_len // 2:
    if (index + 2 < array_len):
        input_array[index], input_array[index + 1] = input_array[index + 1], input_array[index]
    index = index + 2

print(input_array)