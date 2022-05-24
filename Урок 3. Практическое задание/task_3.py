"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

def my_func1(a, b, c):
    return a + b + c - min(a, b, c)

def my_func2(a, b, c):
    my_list = [a, b, c]
    my_list.sort(reverse=True)
    return my_list[0] + my_list[1]

a = int(input("Введите целое чсило a = "))
b = int(input("Введите целое чсило b = "))
c = int(input("Введите целое чсило c = "))

print(my_func1(a, b, c))
print(my_func2(a, b, c))
