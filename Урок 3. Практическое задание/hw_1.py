arg_1 = int(input("Введите числитель: "))
arg_2 = int(input("Введите знаменатель: "))
def my_fun(arg_1, arg_2):
    try:
        res = arg_1 / arg_2
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'
    return res


print(my_fun(arg_1, arg_2))

