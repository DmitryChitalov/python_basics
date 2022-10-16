my_list = [1, None, True, 1.1]


def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return


my_type(my_list)
