def my_func(x, y):
    if x == 0 and y != 0:
        return 0
    res = 1
    for i in range(abs(y)):
        res = res * x if y >= 0 else res / x
    return res


num = float(input('input num: '))
degree = int(input('input degree: '))
print(f"{num} ** {degree} = {my_func(num,degree)}")
