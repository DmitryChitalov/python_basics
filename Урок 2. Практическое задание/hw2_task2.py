my_list = input("Введите целые числа через запятую: ").split(',')
a = 0
b = 1
while len(my_list) > b:
    my_list[a], my_list[b] = my_list[b], my_list[a]
    a += 2
    b += 2
print('Результат: ', my_list)
