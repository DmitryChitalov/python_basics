my_1 = input("введите число:").split(' ')
i, j = 0, 1
while len(my_1) > j:
    my_1[i], my_1[j] = my_1[j], my_1[i]
    i += 2
    j += 2
print('ответ', *my_1)
