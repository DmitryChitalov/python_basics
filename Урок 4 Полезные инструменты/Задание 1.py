"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета
для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

winhrs, phrs, prize = int(argv[1]), int(argv[2]), int(argv[3])


def payment(win, ph, pr):
    """
    Функция выполняет расчет заработной платы сотрудника
    (int, int, int) -> int

    :param win: выработка в часах
    :param ph: ставка в час
    :param pr: премия
    :return: расчет заработной платы сотрудника
    #>>> python3 Задание\ 1.py 10 20 30
    Your salary calculations: 230
    """

    return (win * ph) + pr


print(f'Your salary calculations: {payment(winhrs, phrs, prize)}')
