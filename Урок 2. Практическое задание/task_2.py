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
user_vals = input('Введите целые числа через пробел: ').split(' ')
lenght = len(user_vals)
odd = lenght % 2 != 0
reodered_array = []
for i in range(lenght):
    if i == lenght - 1 and odd:
        current_val = user_vals[i]
        reodered_array.append(current_val)
    elif (i + 1) % 2 != 0:
        next_val = user_vals[i + 1]
        current_val = user_vals[i]
        reodered_array.append(next_val)
        reodered_array.append(current_val)
print(f'Результат: {" ".join(str(x) for x in reodered_array)}')
