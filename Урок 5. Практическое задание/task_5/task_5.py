"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

# pylint: disable=line-too-long

SIMPLE_DIGIT = "2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101"

with open("my_file.txt", "w+", encoding='utf-8') as file:

    file.writelines(SIMPLE_DIGIT)
    num = SIMPLE_DIGIT.split()
    print(f"Сумма чисел: {sum(map(int,num))}")
