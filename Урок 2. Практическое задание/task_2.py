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
# while
user_list = list(map(int, input('Введите целые числа через пробел : ').split(' ')))
while_rez_list = []

i = 0
if len(user_list) % 2 == 0:
    while i < len(user_list) - 1:
        while_rez_list.append(user_list[i + 1])
        while_rez_list.append(user_list[i])
        i = i + 2
else:
    item = user_list.pop(len(user_list) - 1)
    while i < len(user_list) - 1:
        while_rez_list.append(user_list[i + 1])
        while_rez_list.append(user_list[i])
        i = i + 2
    while_rez_list.append(item)

print(while_rez_list)

# for
user_list = list(map(int, input('enter list : ').split(' ')))
for_rez_list = []

if len(user_list) % 2 == 0:
    for i in range(0, len(user_list) - 1, 2):
        for_rez_list.append(user_list[i + 1])
        for_rez_list.append(user_list[i])
else:
    item = user_list.pop(len(user_list) - 1)
    for i in range(0, len(user_list) - 1, 2):
        for_rez_list.append(user_list[i + 1])
        for_rez_list.append(user_list[i])
    for_rez_list.append(item)

print(for_rez_list)
