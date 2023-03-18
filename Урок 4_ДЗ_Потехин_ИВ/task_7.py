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


# задаем функицю определения факториала
def fact(n):
    my_list = []
    factor = 1
    for x in count(1):
        if x > n:
            break
        factor = factor * x
        yield factor
        my_list.append(factor)
    print(f'Последовательность: {my_list}')


# ввод параметра
n = int(input('Введите целое число: '))
# доп параметр для вывод числа
i = 1
#
for el in fact(n):
    print(f'Факториал {i} = {el}')
    i += 1
