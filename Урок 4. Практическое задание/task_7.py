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

import string_extension

def fact(num):
    iterator = 1
    factorial = 1
    while iterator <= num:
        factorial = factorial * iterator
        yield iterator, factorial
        iterator += 1

input_str = input("Please, inpur integer number: ")

if string_extension.is_int(input_str):
    number = int(input_str)

    for ndx, el in fact(number):
        print(f"{ndx}! = {el}")
else:
    print("Error: your input value is not a integer number")