"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random

a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
c = int(input("Введите количество чисел: "))
with open("t5.txt", "w+") as t_obj:
    print(*[random.randint(a, b) for i in range(c)], file=t_obj)
    t_obj.seek(0)
    print("Сумма чисел в файле:", sum(map(int, t_obj.read().split())))