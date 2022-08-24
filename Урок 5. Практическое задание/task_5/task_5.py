"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

f = open('file_task_5.txt', 'w')
print("Введите набор чисел, разделенных пробелами: ")
while True:
    text = input()
    f.write(text + '\n')
    if text == "":
        break

f = open('file_task_5.txt', 'r')
list = f.read().split()
total = 0
for elem in list:
    total += float(elem)
print("Сумма чисел в файле: ", total)
f.close()