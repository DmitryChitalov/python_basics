from math import factorial

n = int(input("Введите число N: "))


def fact(a):
    for el in range(1, a + 1):
        print(el, end='! = ')
        yield factorial(el)


for el in fact(n):
    print(el)
