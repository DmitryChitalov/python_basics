"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open(r"C:\Users\Serg\Desktop\ddd.txt", 'w', encoding="utf-8") as my_file:
    my_file.write(input('Введите числа через пробел: '))
with open(r"C:\Users\Serg\Desktop\ddd.txt", 'r', encoding="utf-8") as my_file_2:
    text = list(my_file_2.read().split(" "))
    sum_num = 0
    for el in range(len(text)):
        sum_num += int(text[el])
    print(sum_num)
