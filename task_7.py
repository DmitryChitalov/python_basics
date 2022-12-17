from math import factorial

def fact(n):
    '''Функция создает генератор чисел от 1
    до n и возвращает их факториалы.'''

    for el in range(1, (n + 1)):
        yield factorial(el)

for el in fact(5):
    print(el)