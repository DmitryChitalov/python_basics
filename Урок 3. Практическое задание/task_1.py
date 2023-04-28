def my_func(var_1, var_2):
    try:
        return var_1/var_2
    except ZeroDivisionError as e:
        print(f'Делить на ноль нельзя')

print(my_func(int(input('Введите делимое: ')) , int(input('Введите делитель:'))))









