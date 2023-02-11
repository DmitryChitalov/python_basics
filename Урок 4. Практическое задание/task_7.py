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
    for num in range(1, n + 1):
        yield num
try:
    n = int(input('Введите неотрицательное целое число: '))
except ValueError as e:
    print(f'Вы ввели значение некорректно!\nОшибка: {e}')
else:
    if n >= 0:
        result = 1
        for el in fact(n):
            result *= el
        print(f'!{n} = {result}')
    else:
        print('Вы ввели значение некорректно!')