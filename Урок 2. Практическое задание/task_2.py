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

list_new_elem = input("Введите целые числа через пробел: ").split(' ')

list_elem = []
for el in list_new_elem:
    list_elem.append(int(el))

# Альтернативный вариант
# list_elem = [1, 2, 3, 4, 5, 7, 9]
mv_list = []
elem_in_array = 0

if len(list_elem) % 2 == 0:
    for el in range(len(list_elem) // 2):
        mv_list.append(list_elem[elem_in_array + 1])
        mv_list.append(list_elem[elem_in_array])
        elem_in_array += 2
elif len(list_elem) % 2 != 0:
    for el in range(len(list_elem) // 2):
        mv_list.append(list_elem[elem_in_array + 1])
        mv_list.append(list_elem[elem_in_array])
        elem_in_array += 2
    mv_list.append(list_elem[-1])
print(mv_list)
