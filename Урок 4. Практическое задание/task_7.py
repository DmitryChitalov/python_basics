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


def fact(num):
    for el in range(1, num + 1):
        yield el


num = 5

# Вариант первый через функцию
for elem in fact(num):
    nums = str(['* ' + str(el) for el in range(2, elem + 1)])
    nums = nums.replace('[', '').replace(']', '').replace("'", '').replace(',', '')
    print(f"Факториал числа {elem}! = 1 {nums} = {factorial(elem)}")

print("")

# Вариант второй (альтернативный метод)
nums = str(['* ' + str(el) for el in range(2, num + 1)])
nums = nums.replace('[', '').replace(']', '').replace("'", '').replace(',', '')
print(f"Факториал числа {num}! = 1 {nums} = {factorial(num)}")
