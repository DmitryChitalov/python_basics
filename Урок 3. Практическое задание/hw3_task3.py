arg_1 = int(input("Введите первое число: "))
arg_2 = int(input("Введите второе число: "))
arg_3 = int(input("Введите третье число: "))


def my_func():
    return (arg_1 + arg_2 + arg_3) - min(arg_1, arg_2, arg_3)


print(f"Сумма наибольших двух аргументов: {my_func()}")
