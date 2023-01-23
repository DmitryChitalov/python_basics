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
""" Решение к заданию №2 """ 
g = int(input("How many items in list do you want to add?\n\t Enter items quantity: "))
my_lst = []
for i in range(g):
    my_lst.append(input(f"Item # {i + 1} : "))
print(f"Your item list view:\n{my_lst}")
for x in range(0, (len(my_lst) - 1),2):
    my_lst[x], my_lst[x+1] = my_lst[x+1], my_lst[x]
print(f"Your CHANGED item list view:\n{my_lst}")

