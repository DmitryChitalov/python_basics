my_list = input('Введите элементы списка: ').split(' ')
i = 0
j = 1
while j < len(my_list):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    i += 2
    j += 2
print(my_list)