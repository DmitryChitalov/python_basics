"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
open_file = open("task_file5.txt", "w+")
open_file.write(input("Введите в строку числа через пробел: "))
open_file.seek(0)
file_content = open_file.readline()
my_list = file_content.split()
result = 0

for el in my_list:
    print(el)
    result += int(el)

open_file.close()
print(f"Сумма чисел: {result}")

"""
Введите в строку числа через пробел: 34 54 12 33 51 78 99 52
34
54
12
33
51
78
99
52
Сумма чисел: 413
"""