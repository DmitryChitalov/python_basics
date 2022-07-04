"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

print("Cумма наибольших двух аргументов")
var_1 = int(input("Аргумент 1: "))
var_2 = int(input("Аргумент 2: "))
var_3 = int(input("Аргумент 3: "))

''' Вариант 1, c sort '''
def my_func(var_1, var_2, var_3):
    a = [var_1, var_2, var_3]
    b = sorted(a, reverse=True)
    b.pop(2)
    res = sum(b)
    return res
print("Вариант 1, c sort:", my_func(var_1, var_2, var_3))

''' Вариант 2, без sort '''
def my_func(var_1, var_2, var_3):
    a = [var_1, var_2, var_3]
    b = sum(a) - min(a)
    return b
print("Вариант 2, без sort:", (my_func(var_1, var_2, var_3)))
