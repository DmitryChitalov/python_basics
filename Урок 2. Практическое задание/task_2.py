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

u_list = input('Введите целые числа через пробел: ').split()
for a in range(0, len(u_list)-1, 2):
    u_list[a], u_list[a+1] = u_list[a+1], u_list[a]
print(f"Результат: {u_list}")