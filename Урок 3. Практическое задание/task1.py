def my_func(a, b):
    if b == 0:
        print("Делить на 0 нельзя!")
    else:
        return a / b

a = int(input("Введите числа a и b:\na: "))
b = int(input("b: "))
print(my_func(a, b))
