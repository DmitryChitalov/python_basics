"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
new_numbs = []
with open('file.txt', 'w', encoding='utf-8') as my_f:
    new_numbs = (input("Введите набор чисел через пробел: "))
    my_f.write(new_numbs)
total = 0
with open('file.txt', 'r', encoding='utf-8') as my_f2:
    data = my_f2.read().split()
    numbers = [int(x) for x in data]
    for x in numbers:
        total += x
    print(total)
