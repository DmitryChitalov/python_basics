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
ls = input('Введите целые числа через пробел: ')
ls = ls.split()

idx = 0
while idx + 1 < len(ls):
    var1, var2 = ls[idx], ls[idx + 1]
    ls[idx], ls[idx + 1] = var2, var1
    idx += 2

print(' '.join(ls))
