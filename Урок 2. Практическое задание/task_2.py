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
my_list = input("Введите целые числа через пробел:").split(" ")

new_list = []
for i in range(0, len(my_list), 2):
    if i != len(my_list)-1:
        new_list.append(my_list[i+1])
        new_list.append(my_list[i])
    else:
        new_list.append(my_list[i])
print(new_list)