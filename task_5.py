my_list = [6, 4, 8, 2, 1, 1, 7, 5]
number = int(input("Введите натуральное число: "))
if my_list.count(number) > 0:
    my_list.insert((my_list.index(number) + my_list.count(number)), number)
    print(my_list)
else:
    print(my_list.append(number))