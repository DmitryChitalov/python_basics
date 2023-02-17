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
my_list_first = input('Введите элементы списка: ').split()
ind_el = 0
for i in range(int(len(my_list_first) / 2)):
    my_list_first[ind_el], my_list_first[ind_el + 1] = my_list_first[ind_el + 1], my_list_first[ind_el]
    ind_el +=2
print(' '.join(my_list_first))

my_list_second = input('Введите элементы списка: ').split()
for index, value in enumerate(my_list_second):
    if index + 2 > len(my_list_second):
        break 
    elif index % 2 == 0:
        my_list_second[index], my_list_second[index + 1] = my_list_second[index + 1], my_list_second[index]
print(' '.join(my_list_second))