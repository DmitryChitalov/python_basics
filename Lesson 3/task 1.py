
def my_func(*args):
    try:
        arg_1 = int(input("делимое число: "))
        arg_2 = int(input("делитель: "))
        res = arg_1 // arg_2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Нельзя использовать ноль в качестве делителя!"
    return res
print (f'result {my_func()}')