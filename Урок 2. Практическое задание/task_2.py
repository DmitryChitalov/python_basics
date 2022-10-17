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

user_data = input("Введите целые числа через пробел: ")

user_list_str = user_data.split(' ')
user_list_int = [int(i) for i in user_list_str]

print(user_list_int)

iter_cont = len(user_list_int) - 1
if iter_cont > 0:
    current_index = 0
    while current_index < iter_cont:
        user_list_int[current_index], user_list_int[current_index + 1] = \
            user_list_int[current_index + 1], user_list_int[current_index]
        current_index += 2

print(user_list_int)
