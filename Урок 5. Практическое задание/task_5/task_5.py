"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint

with open("task_5.txt", "w+", encoding='utf-8') as rand:
    print(*[randint(1, 1000) for i in range(20)], file=rand)
    rand.seek(0)
    print("Сумма чисел в файле:", sum(map(int, rand.read().split())))
