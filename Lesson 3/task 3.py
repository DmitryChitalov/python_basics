
def my_func(var_1, var_2, var_3):
    if var_1 >= var_3 and var_2 >= var_3:
        return var_1 + var_2
    elif var_1 > var_2 and var_1 < var_3:
        return var_1 + var_3
    else:
        return var_1 + var_3

print(f'Result - {my_func(int(input("enter first argument ")), int(input("enter second argument ")), int(input("enter third argument ")))}')