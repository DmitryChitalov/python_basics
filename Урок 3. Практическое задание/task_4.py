def my_pow(x, y):
    return 1 / (x ** abs(y))


x = int(input('Input "x": '))
y = int(input('Input "y": '))


result_my_pow = my_pow(x, y)
print('Result:', result_my_pow)
