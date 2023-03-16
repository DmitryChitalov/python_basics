
def power(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res


print(power(float(input("Первое значение - ")), int(input("Второе значение - "))))

# я не совсем понял как решить задачу через my_func(x, y)
