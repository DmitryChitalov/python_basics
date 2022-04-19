from itertools import count


def fact(n):
    fac = 1
    for el in count(1):
        if el > n:
            break
        fac = fac * el
        yield fac


a = int(input("введите число - "))
i = 0
for el in fact(a):
    i += 1
    print(f"{i}! = {el}")
