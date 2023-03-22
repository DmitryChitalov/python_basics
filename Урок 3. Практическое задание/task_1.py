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
#!/usr/bin/env python3
user_input_a = int(input("Пожалуйста, ввдедите первое число: "))
user_input_b = int(input("Пожалуйста, ввдедите второе число: "))

def user_division(user_input_a, user_input_b):
    try:
        return user_input_a / user_input_b
    except ZeroDivisionError:
        print("Не пытайтесь делить на ноль. Это сводит компьютер с ума.")
        return " "

print(user_division(user_input_a, user_input_b))