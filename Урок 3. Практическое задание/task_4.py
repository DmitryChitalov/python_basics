def my_func_1(x, y):
    rez = x ** y
    return rez


def my_func_2(x, y):
    a = abs(y)
    b = 1
    i = 0
    while a > i:
        b = b * x
        i += 1
    rez = 1 / b
    return rez


a = int(input("введите целое положительное число "))
if a < 0:
    print("вы ввели отрицательное число")
    exit()
b = int(input("введите целое отрицательное число "))
if b >= 0:
    print("вы ввели положительное число")
    exit()

print(my_func_1(a, b))
print(my_func_2(a, b))