my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(my_list)
print([el for i, el in enumerate(my_list) if i>0 and my_list[i] > my_list[i - 1]])