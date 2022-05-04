def func():
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    if a < b: min = a
    else: min = b
    if c < min: min = c
    d = a + b + c - min
    return d
print(func())
