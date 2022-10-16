'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''


def func():
    try:

        arg1 = int(input("Введите аргумент №1 = "))
        arg2 = int(input("Введите аргумент №2 = "))
        result = arg1 / arg2

    except ValueError:
        return "ValueError"
    except ZeroDivisionError:
        return "ZeroDivisionError"
    return result


print(f'Результат деления = {func()}')
