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


def fact(num):
    for el in range(1, num + 1):
        yield el


n = int(input("Введите число: "))
factorial = 1
raschet = ''
for element in fact(n):
    factorial *= element
    if element < n:
        raschet += str(element) + " * "
    else:
        raschet += str(element)
print(f"факториал {n}! = {raschet} = {factorial}")
"""
Введите число: 4
факториал 4! = 1 * 2 * 3 * 4 = 24

Process finished with exit code 0
"""
