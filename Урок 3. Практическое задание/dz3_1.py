# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль

def my_func(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "деление на ноль!"


print(my_func(int(input("Enter x = ")), int(input("Enter y = "))))
