"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

inp = input(
    'Enter your name, surname, year of birth, city of leaving, email, telephone number: ').split()


def data(n, s, yb, cl, e, tn):
    """
    Функция принимает и выводит данные о пользователе

    Параметры: n - name, s - surname, yb - year of birth, cl - city of leaving, e - email, tn - telephone.
    (str) -> str

    #>>> print(*data(n=inp[0], s=inp[1], yb=inp[2], cl=inp[3], e=inp[4], tn=inp[5]))
    W Www 1990 Moscow ggg@prot.mail +799911111111
    """

    return n, s, yb, cl, e, tn


print(*data(n=inp[0], s=inp[1], yb=inp[2], cl=inp[3], e=inp[4], tn=inp[5]))
