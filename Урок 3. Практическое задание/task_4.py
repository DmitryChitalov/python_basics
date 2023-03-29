def my_func(x, y):
    if y == 0:
        return 1
    y = abs(y)
    return x * my_func(x, y-1)
while True:
    try:
        x = float(input("Введите действительное положительное число x: "))
        if x < 0:
            raise Exception()
        y = int(input("Введите целое отрицательное число y: "))
        if y > 0:
            raise Exception()
        print(1 / my_func(x, y))
        break
    except Exception as e:
        print('Неверный формат')


"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""
