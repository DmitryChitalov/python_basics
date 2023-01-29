def my_func(x, y):
    res = 1
    while y > 0:
        res = res * x
        y = y-1
    return res

print(my_func(
    x=int(input('Введите х: ')),
    y=int(input('Введите у: '))
))
