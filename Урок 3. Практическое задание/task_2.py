"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

"""
2. Реализовать функцию, принимающую два числа (позиционные аргументы)
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
"""


def division():
    try:
        var_a / var_b
        res = round(var_a / var_b, 2)
    except ZeroDivisionError:
        return "Вы что? Пытаетесь делить на 0!"
    return res


try:
    var_a = int(input("Введите первое число: "))
    var_b = int(input("Введите второе число: "))
    print(division())
except ValueError:
    print("Введите цифры")
