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


# Создадим функцию ввода и проверки зачения на число
def __input_and_div_num(first_num, second_num):
    while True:
        try:
            summ_num = first_num/second_num
            print(f'Результат деления: {"{:.3f}".format(summ_num)}')
            return 0

        except ZeroDivisionError:
            print('Знаминатель не должен быть нулевым!\n'
                  ' Введите знаминатель:')
            second_num = float(input())


# Выводим название программы
print('Программа выполняющая деление двух чисел')

__input_and_div_num(first_num=float(input('Введите числитель: ')),
                      second_num=float(input('Введите знаминатель: ')))
