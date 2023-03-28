"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""
#!/usr/bin/env python3
user_input_x = int(input("Пожалуйста, введите действительное положительное число: "))
user_input_y = int(input("Пожалуйста, введите целое отрицательное число: "))
print(f"Мы с Питоном возведем число {user_input_x} в степень {user_input_y}.")

def my_func(user_input_x, user_input_y):
    while user_input_y < -1:
        user_input_x = user_input_x * user_input_x
        user_input_y = user_input_y + 1
    calc_result = 1.0 / user_input_x
    return calc_result

print(my_func(user_input_x, user_input_y))
print(f"Проверим функцией pow(). Результат: {pow(user_input_x, user_input_y)}")
