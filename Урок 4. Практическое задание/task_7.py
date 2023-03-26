"""
7. Реализовать генератор с помощью функции с ключевым словом yield,
 создающим очередное значение.

 При вызове функции должен создаваться объект-генератор.
 Функция должна вызываться следующим образом: for el in fact(n).
 Функция отвечает за получение факториала числа,
 а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from math import factorial


def my_func(num):
    """
    Функция отвечает за получение факториала числа
    :param Число для вычисления
    :return: Факториала числа
    """
    print(f"Факториал числа {num}! = ", end='')
    for i in range(1, num + 1):
        print(f"({factorial(i - 1)}*{i})=", end='')
        yield factorial(i)
    print(f"= {factorial(i)}")


try:
    my_number = int(input('Введите число: '))
except ValueError:
    print("Ошибочный ввод!")
else:
    for el in my_func(my_number):
        print(el, end=' ')
