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
from itertools import count


def fact(n):
    b = 1
    for a in count(1):
        if a > n:
            break

        b = b * a
        yield b


n = int(input("Введите число: "))
for el in fact(n):
    print(el)
