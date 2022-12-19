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
#Task_1
def division(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        return "куда ты делишь?"
num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
print(division(num_1, num_2))
