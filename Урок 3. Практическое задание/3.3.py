# Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    '''
    Функция принимает три числа, находит два наибольших и суммирует их
    :param arg1: первое число
    :param arg2: второе число
    :param arg3: третье число
    :return: возвращает результат суммирования
    '''
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 >= arg2 and arg3 >= arg2:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'сума двух наибольших= {my_func(int(input("первое число: ")), int(input("второе число: ")), int(input("третье число: ")))}')
