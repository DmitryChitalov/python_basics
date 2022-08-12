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

# Выводим название программы
print('Программа выполняющая деление двух чисел')

# Создадим функцию ввода и проверки зачения на число


def __input_and_check_num(text):
    temp_in = input(text)
    while True:
        try:
            temp_in = float(temp_in)
            return temp_in

        except Exception:
            print('Введите число ')
            temp_in = input()
            continue

# Определяем переменные
first_num = __input_and_check_num('Введите числитель: ')
second_num = __input_and_check_num('Введите знаминатель: ')

# Проверяем возможность деления и выводим результат
try:
    div_num = first_num / second_num
    print(f'Результат деления: {"{:.3f}".format(div_num)}')
except ZeroDivisionError:
    print('Нельзя делить на ноль!')
