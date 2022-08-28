"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open("test.txt", 'w', encoding="utf-8") as input_file:
    input_file.write(input('Введите числа через пробел: '))
with open("test.txt", 'r', encoding="utf-8") as output_file:
    text = list(output_file.read().split(" "))
    sum_num = 0
    for el in range(len(text)):
        sum_num += int(text[el])
    print(sum_num)
