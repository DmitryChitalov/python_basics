"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func(x, y, z):
    max = 0
    for i in [x, y, z]:
        if i > max:
            max = i
    return max


print(my_func_sort(2, -2, 5))
print(my_func(2, -2, 8))
