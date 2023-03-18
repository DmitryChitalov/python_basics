"""

Задание 2. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

"""
def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print(f'Деление на 0, странная затея')

number_1 = int(input('Введите первое число : '))
number_2 = int(input('Введите второе число : '))
result = division(number_1, number_2)
if result is None:
    pass
else:
    print(result)