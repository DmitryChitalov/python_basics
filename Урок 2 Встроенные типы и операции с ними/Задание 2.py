"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

l = input('Введите цифры через пробел: ').split()
n_1 = 1
n_2 = 2
for i in range(len(l)):
    if n_2 < len(l):
        if i == 0:
            l[i], l[i + 1] = l[i + 1], l[i]
        else:
            l[n_2], l[n_1] = l[n_1], l[n_2]
            n_1 += 1
            n_2 += 1
        n_1 += 1
        n_2 += 1
print(l)

"""
Введите цифры через пробел: 6 7 8 9 0
['7', '6', '9', '8', '0']

Process finished with exit code 0
"""
