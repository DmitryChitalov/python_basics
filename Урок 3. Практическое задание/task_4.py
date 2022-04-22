def func(x,y):
    a = x ** y
    b = 1
    c = 1
    while c <= abs(y):
        b *= x
        c += 1

    return a, 1 / b
print(func(int(input("1 положительное число: ")), int(input("2 отрицательное число: "))))
