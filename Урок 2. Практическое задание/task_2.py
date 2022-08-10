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

# Выводим название программы
print(f'Программа обмена значений соседних элементов списка ')

# Запрашиваем исходные данные и преобразовываем в список
my_list = input('Введите набор чисел через пробел: ').split(' ')

# Арифметичекие преобразования и перемещение элементов списка
my_list_len = len(my_list)
for index_in_list in range(0, my_list_len-1, 2):
    my_list[index_in_list], my_list[index_in_list+1] = my_list[index_in_list+1], my_list[index_in_list]

# Вывод результата
print(f'Список после перестанвок:')
print(" ".join(my_list))
