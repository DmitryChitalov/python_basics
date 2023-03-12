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
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
def func(number1, number2):
    try:
        res = number1 / number2
    except ZeroDivisionError:
        return "Вы что? Пытаетесь делить на 0!"
    return(res)

    if number2 != 0:
        return number1 / number2
    else:
        print("Вы что? Пытаетесь делить на 0!")
print(f'result  {func(number1, number2)}')
