"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""
#
def my_func(x, y):
    i = 0
    temp = 1.0
    result = 0.0
    if y < 0:
        while i > y:
            temp = temp * x
            i -= 1
            result = 1 / temp
    else:
        while i < y:
            temp = temp * x
            i += 1
            result = temp
    return round(result, 7)

while True:
    try:
        input_usr_x = int(input('Введите число x: '))
        if input_usr_x < 0:
            print('Нужное ввести положительное число') 
            continue
        input_usr_y = int(input('В какую степень хотите возвести: '))
        break
    except ValueError:
        print('Нужно ввести число')
    

print('Результат: ', my_func(input_usr_x, input_usr_y))