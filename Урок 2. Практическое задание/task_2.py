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
noname_list = input("Введите целые числа через пробел: ").split(' ')
i = 0
k = 1

while len(noname_list) > k:
    noname_list[i], noname_list[k] = noname_list[k], noname_list[i]
    i += 2
    k += 2

print("Результат: ", *noname_list)
