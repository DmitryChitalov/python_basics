def my_sum():
    var_1 = int(input('Put number 1: '))
    var_2 = int(input('Put number 2: '))
    var_3 = int(input('Put number 3: '))
    if var_1 < var_2 < var_3:
        return var_2 + var_3
    if var_1 < var_3 < var_2:
        return var_2 + var_3
    if var_2 < var_1 < var_3:
        return var_1 + var_3
    if var_2 < var_3 < var_1:
        return var_1 + var_3
    if var_3 < var_1 < var_2:
        return var_1 + var_2
    if var_3 < var_2 < var_1:
        return var_1 + var_2


func_obj = my_sum()
print(func_obj)
