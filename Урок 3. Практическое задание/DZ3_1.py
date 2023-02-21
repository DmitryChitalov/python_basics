def my_division(var_1, var_2):
    try:
        my_res = var_1 / var_2
    except ZeroDivisionError:
        print('Введено значение 0. Ошибка ввода')
        return
    my_res = var_1 / var_2
    return my_res
print(my_division(float(input('Введите делимое: ')), float(input('Введите делитель: '))))