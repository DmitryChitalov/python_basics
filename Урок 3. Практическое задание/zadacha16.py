# Требуется вычислить, сколько раз встречается некоторое число X в массиве 
# из случайных чисел. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint
N = int(input())
list_1 = [randint(0, 10) for i in range(N)]
print(list_1)
X = int(input())
count = 0
for i in range(len(list_1) - 1):
    if list_1[i] == X:
        count += 1
print(count)