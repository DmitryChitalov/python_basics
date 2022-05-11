from itertools import count
from itertools import cycle
from random import randint


def script1(a, b):
    rez = []
    for el in count(a):
        if el > b:
            break
        else:
            rez.append(el)
    return rez


def script2(*args):
    cou = 0
    rez = []
    for el in cycle(args):
        if cou >= len(args):
            break
        rez.append(el)
        cou += 1
    return rez


lenght = int(input("Введите длинну исходного списка "))
my_string = [randint(0, 20) for el in range(0, lenght)]
a = int(input("введите первое число последовательности - "))
b = int(input("введите последнее число последовательности - "))
print(f"итератор, генерирующий целые числа, начиная с указанного - {script1(a, b)}")
print(f"исходная строка - {my_string}")
print(f"итератор, повторяющий элементы исходного списка - {script2(*my_string)}")
