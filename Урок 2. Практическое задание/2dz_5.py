# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_num = int(input("Введите число: "))
my_list = [7, 4, 3, 2]
c = my_list.count(my_num)
for elem in my_list:
    if c > 0:
        i = my_list.index(my_num)
        my_list.insert(i + c, my_num)
        break
    else:
        if my_num > elem:
            j = my_list.index(elem)
            my_list.insert(j, my_num)
            break
        elif my_num < my_list[len(my_list) - 1]:
            my_list.append(my_num)
print(my_list)
