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
str_list = input("Введите значение списка чисел через пробел: ")
my_list = str_list.split()
result_list = []
index_list = 0
count_list = len(my_list) - 1
for n in my_list:
    if index_list % 2 == 0:
        if index_list < count_list:
            result_list.append(int(my_list[index_list + 1]))
            result_list.append(int(n))
        else:
            result_list.append(int(n))
    index_list += 1
print(f"Исходный:  {my_list}")
print(f"Результат: {result_list}")
