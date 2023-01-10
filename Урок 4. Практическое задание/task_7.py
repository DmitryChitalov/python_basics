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

def fact(user_inp):
    factorial = 1
    for el in count(1):
        if el > user_inp:
            break
        factorial = factorial * el
        yield factorial

user_input = int(input('Введите не отрицательное число: '))

counter = 0

for i in fact(user_input):
    counter += 1
    print(counter,'=', i)

