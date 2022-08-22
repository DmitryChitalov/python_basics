"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open('task_5.txt', 'w', encoding='utf-8') as file:
    line = input('Enter numbers through space ')
    file.writelines(line)
    numbers = line.split()
    print(sum(map(int, numbers)))