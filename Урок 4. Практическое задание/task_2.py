my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[i] for i in range(len(my_list)) if my_list[i-1] < my_list[i]]
print("Исходный список: " + str(my_list))
print("Новый список: " + str(new_list))
