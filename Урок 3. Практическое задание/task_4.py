def my_func(x, y):
    if y == 0:
        return 1
    elif y > 0:
        result = x
        for i in range(1, y):
            result *= x
        return result
    else:
        result = 1
        for i in range(y, 0):
            result /= x
        return result


print(my_func(4, -5))
