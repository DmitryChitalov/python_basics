"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

file_name = "out_file.txt"

try:
    with open(file_name, "w") as out_file:
        n = input("> ")
        while n != '':
            out_file.write(n + ' ')
            n = input("> ")
except IOError:
    print(f"Ошибка записи файла {file_name}!")
    exit(1)

total = 0
try:
    with open(file_name) as in_file:
        values = in_file.readline().split(' ')
        print(f"Найдены числа: {values}")
    for el in values:
        try:
            total += int(el)
        except ValueError:
            pass
    print(f"Сумма чисел в файле: {total}")

except IOError:
    print(f"Ошибка чтения файла {file_name}!")
    exit(1)
