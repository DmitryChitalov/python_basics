"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""

def my_func(x:int,y:int):
    """
    Return x**y with and without built-in function.

    :param x: Positive integer
    :param y: Negative integer
    :return: Two floats. Result of x**y without using built-in function and another one using 
    it for reference
    """

    # Do not use built-in function:
    if not x >=0 or not y <=0:
        print("First number must be more than 0, scond number must be less than 0")
        exit(0)
    elif isinstance(x, int) or isinstance(y, int):
        print("Wrong number type, must be integer")
        exit(0)

    y_module = y * -1           # convert y to positive for further use
    result = x                  # set result to x temporarily

    for i in range(1,y_module): # get x in power of y
        result *= x

    result = 1 / result         # get final result by dividing 1 by x in power of y


    #use built-in function
    result2 = x**y

    return f"without built-in finction : {result} \nwith built-in finction    : {result2}"


x,y = int(input("1st number:")),int(input("2nd number:"))   # ask for user input

print(my_func(x,y))
