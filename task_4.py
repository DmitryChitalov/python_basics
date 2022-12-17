my_list = [20, 20, 1, 311, 11, 45, 11, 0, 8, 1]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)