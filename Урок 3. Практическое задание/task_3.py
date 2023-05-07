def my_func(a, b, c):
    if a <= b and a <= c:
        return b + c
    elif b <= c:
        return a + c
    else:
        return a + b


a = int(input('Input "a": '))
b = int(input('Input "b": '))
c = int(input('Input "c": '))

my_sum = my_func(a, b, c)
print('Max sum', my_sum)