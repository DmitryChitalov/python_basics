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

user_list = input('Введите целый числа: ')

user_list = list(user_list)
user_copy = user_list.copy()

ind = 0

number_del = len(user_copy) % 2

if number_del == 0:
    while ind < len(user_copy):
        user_copy[ind] = user_list[ind + 1]
        user_copy[ind + 1] = user_list[ind]

        ind += 2

elif number_del != 0:

    while ind < len(user_copy) - 1:
        user_copy[ind] = user_list[ind + 1]
        user_copy[ind + 1] = user_list[ind]

        ind += 2

print(user_copy)
