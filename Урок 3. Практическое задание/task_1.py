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


def div_of_two(num1, num2):
    return num1 / num2


param1 = float(input("Введите первое число: "))
flag = True
while flag:
    try:
        param2 = float(input("Введите второе число: "))
        if param2 == 0:
            raise ValueError()
        print(f"Результат деления: {div_of_two(param1, param2)}")
        flag = False
    except Exception:
        print("делить на ноль нельзя, лол, давай еще раз")
