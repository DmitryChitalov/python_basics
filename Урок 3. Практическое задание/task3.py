def my_func(a, b, c):
    return max(sum([a, b]), sum([a, c]), sum([b, c]))

a = int(input("Введите числа:\na = "))
b = int(input("b = "))
c = int(input("c = "))

print(f"Наибольшая сумма: {my_func(a, b, c)}")