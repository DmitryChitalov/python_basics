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


def solution(*args):
    # Выводим исключения
    try:
        num1 = float(input("Введите первое число:"))
        num2 = float(input("Введите второе число:"))
        result = num1 / num2
    except ValueError:
        return 'Ошибка!Вводите только числа'
    except ZeroDivisionError:
        return 'Нельзя использовать ноль'
    return result


print(f'Рзультат: {solution()}')
