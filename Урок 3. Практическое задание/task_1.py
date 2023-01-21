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


def dividing_numbers(number_one, number_two):
    try:
        return number_one / number_two
    except ZeroDivisionError:
        return "Вы что? Пытаетесь делить на 0!"


try:
    first_number = float(input("Введите первое число: "))
    sec_number = float(input("Введите второе число: "))
    print(f"Ответ: {dividing_numbers(first_number, sec_number)}")
except ValueError:
    print("Необходимо ввести только числа!")
