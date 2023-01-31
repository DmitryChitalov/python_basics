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
def my_del():
    try:
        num = float(input("Введите число - делимое: "))
        denom = float(input("Введите число - делитель: "))
        result = num / denom
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    except ValueError:
        return "Введенное значение не является числом"
    return result
print(my_del())
