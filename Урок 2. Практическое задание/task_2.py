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

elem_add = []
elem = int(input("Введите количество элементов списка "))
i = 0
e = 0

while i < elem:
    elem_add.append(input("Введите следующее значение списка "))
    i += 1
for elem in range(int(len(elem_add) / 2)):
    elem_add[e], elem_add[e + 1] = elem_add[e + 1], elem_add[e]
    e += 2
print(f"Список после форматирования {elem_add}")
