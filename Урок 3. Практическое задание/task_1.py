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

# первый вариант учет с О

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
def s_ca():
    try:
        return a / b
    except ZeroDivisionError:
        return "Вы что? Пытаетесь делить на 0!"

print(s_ca())



#Вариант 1 (учет 0; строковые вместо чисел)



def s_ca():
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        return a / b
    except ZeroDivisionError:
        return "Вы что? Пытаетесь делить на 0!"
    except ValueError:
        return "ошибка"

print(s_ca())

#Вариант 2
def s_ca1(a, b):
    try:
        a1 = int(a)
        b1 = int(b)
        return a1 / b1
    except ZeroDivisionError:
        return "Вы что? Пытаетесь делить на 0!"
    except ValueError:
        return "ошибка"


a = input("Введите первое число: ")
b = input("Введите второе число: ")


print(s_ca1(a, b))