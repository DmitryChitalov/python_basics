def my_func(a, b, c):
    rez = 0
    if a > b:
        rez = rez + a
    else:
        rez = rez + b
    if c > b:
        rez = rez + c
    else:
        rez = rez + a
    return rez


a = int(input("введите первый аргумент "))
b = int(input("введите второй аргумент "))
c = int(input("введите третий аргумент "))
print(my_func(a, b, c))
