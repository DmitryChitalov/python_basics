"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""
def my_del(num, denom):
    try:
        result = num / denom
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    return result
print(my_del(float(input("Введите число - делимое: ")),
             float(input("Введите число - делитель: "))))
			 
