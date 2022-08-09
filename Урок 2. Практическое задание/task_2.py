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
my_list = input("Введите целые числа через пробел: ").split()
element_index = 0
while element_index < len(my_list) - 1:
    left_element = my_list[element_index]
    right_element = my_list[element_index + 1]
    my_list[element_index] = right_element
    my_list[element_index + 1] = left_element
    element_index += 2

print(f"Результат: ", ' '.join([str(elem) for elem in my_list]))
