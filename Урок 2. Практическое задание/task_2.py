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
sting_for_list = input("Введите целые числа через пробел: ")
my_list = sting_for_list.split()
i = 0
if len(my_list) % 2 == 0:
    while i <= len(my_list):
        temp_value = int(my_list[i])
        my_list[i] = int(my_list[i+1])
        my_list[i+1] = temp_value
        i = i + 2
else:
    while i <= len(my_list) - 2:
        temp_value = int(my_list[i])
        my_list[i] = int(my_list[i+1])
        my_list[i+1] = temp_value
        i = i + 2
print(my_list)
