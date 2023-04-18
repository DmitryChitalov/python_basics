"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
#1)
def my_func(x, y, z):
    my_f = [x, y, z]
    my_f.sort(reverse=True)

    return my_f[0] + my_f[1]
print(my_func(10, 5, 15))


"""
#2)
def my_func(x, y, z):
    if x > y:
        if x > z:
            if y > z:
                return x + y
            else:
                return x + z
        else:
            return x + z
    elif x > z:
        return x + y
    else:
        return z + y
print(my_func(10, 5, 15))
"""