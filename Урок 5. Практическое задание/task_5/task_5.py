"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

file = open('task_5.txt', 'w', encoding='utf-8')
input_line = input('Введите набор чисел через пробел: ')
file.writelines(input_line)
number = input_line.split()
print(f"Сумма введенных вами чисел: {sum(map(int, number))}")
file.close()