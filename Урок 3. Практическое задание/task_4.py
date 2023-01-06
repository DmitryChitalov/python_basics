"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""

numeric = (int, float, complex)
def my_pow(base: numeric, exp: numeric, mod: numeric = None) -> numeric:


    if not isinstance(base, numeric) or not isinstance(exp, numeric):
        raise TypeError(f"unsupported operand type(s) for ** or pow(): "
                        f"'{base.__class__.__name__}' and '{exp.__class__.__name__}'")

    if mod and not isinstance(mod, numeric):
        raise TypeError(f"unsupported operand type(s) for pow(): "
                        f"'{base.__class__.__name__}', '{exp.__class__.__name__}', "
                        f"'{mod.__class__.__name__}'")

    result = 1

    while exp:
        result *= base
        exp -= 1

    if mod is None:
        return result
    else:
        return result % mod


if __name__ == '__main__':
    print(my_pow(3, 6, 4))

