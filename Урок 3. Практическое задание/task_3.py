"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func1(arg_1, arg_2, arg_3):
    my_arr = [arg_1, arg_2, arg_3]
    my_arr.sort()
    return my_arr[1] + my_arr[2]


def my_func2(arg_1, arg_2, arg_3):
    if arg_1 >= arg_2 >= arg_3:
        return arg_1 + arg_2
    elif arg_1 >= arg_3 >= arg_2:
        return arg_1 + arg_3
    elif arg_2 >= arg_3 >= arg_1:
        return arg_2 + arg_3
    elif arg_2 >= arg_1 >= arg_3:
        return arg_1 + arg_2
    elif arg_3 >= arg_1 >= arg_2:
        return arg_3 + arg_1
    else:
        return arg_3 + arg_2


def less3():
    digit_1, digit_2, digit_3 = map(int, input("Введите три числа через пробел: ").split())
    print(f"Сумма двух максимальных элементов: {my_func1(digit_1, digit_2, digit_3)}")
    print(f"Сумма двух максимальных элементов: {my_func2(digit_1, digit_2, digit_3)}")


if __name__ == '__main__':
    less3()

