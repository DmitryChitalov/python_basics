def my_func():
    x = int(input('Input x: '))
    y = int(input('Input y: '))
    if y > 0:
        x = int(abs(x))
        y = round(y * -1, 0)
        return x ** y
    if y < 0:
        x = int(abs(x))
        y = round(y, 0)
        return x ** y


print(my_func())
