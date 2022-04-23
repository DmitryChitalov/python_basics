"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open("text.txt", "w", encoding="utf-8") as my_file:
    a = input("Введите числа через пробел: ")
    my_file.write(a)

with open("text.txt", "r", encoding="utf-8") as my_file:
    a = a.split()
    b = 0
    for el in a:
        b = b + int(el)
    print(f'Сумма: {b}')