# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

print('Введите два числа для выполнения деления')
f_numb = int(input('>'))
s_numb = int(input('>'))


def division(arg_1, arg_2):
    try:
        res = arg_1 / arg_2
    except ZeroDivisionError:
        return "Ошибка. Деление на ноль запрещено"
    else:
        return res


res = division(f_numb, s_numb)
print(f"Результат деления: {res}")