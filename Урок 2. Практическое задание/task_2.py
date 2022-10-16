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
user_list_int = []
for el in user_list_str:
    user_list_int.append(int(el))

print(user_list_int)

iterations = len(user_list_int) - 1
if iterations > 0:
    index = 0
    while index < iterations:
        user_list_int[index], user_list_int[index + 1] = user_list_int[index + 1], user_list_int[index]
        index += 2

print(user_list_int)
