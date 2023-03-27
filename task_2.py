new_lst = input("Введите целые числа через пробел: ").split(' ')
a, b = 0, 1
while len(new_lst) > b:
    new_lst[a], new_lst[b] = new_lst[b], new_lst[a]
    a += 2
    b += 2

print('Итог:', *new_lst)