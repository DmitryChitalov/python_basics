my_list = [5, 50, 16, 47, 0, 1, 3, 9, 4]
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] >
            my_list[i-1]]
print(new_list)