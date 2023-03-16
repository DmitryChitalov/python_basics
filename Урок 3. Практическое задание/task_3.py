def my_func(a, b, c):
    if a >= b and a >= c:
        return a + max(b, c)
    elif b >= a and b >= c:
        return b + max(a, c)
    else:
        return c + max(a, b)


print(f'{my_func(int(input("Введите a: ")), int(input("Введите b: ")), int(input("Введите c: ")))}')

