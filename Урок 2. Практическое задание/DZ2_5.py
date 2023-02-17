my_list = [8, 6, 4, 3, 2, 1]
print(f'Рейтинг - {my_list}')
my_char = int(input('Введите новый элемент рейтинга: '))
if my_list.count(my_char) != 0:
    my_list.reverse()
    pos = my_list.index(my_char)
    my_list.insert(pos, my_char)
    my_list.reverse()
elif my_char == 0:
    my_list.append(my_char)
else:
    i = 0
    while i < len(my_list) + 1:
        if int(my_list[i]) > my_char:
            i += 1
        else:
            my_list.insert(i, my_char)
            break
print(f'Новый рейтинг - {my_list}')