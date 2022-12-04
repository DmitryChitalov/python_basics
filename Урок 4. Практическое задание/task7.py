n = int(input("Введите число: "))

result = 1

def fact(n):
    for el in range(1, n + 1):
        yield el

for el in fact(n):
    result *= el

print(f"{n}! = {result}".format(n = n, result = result))