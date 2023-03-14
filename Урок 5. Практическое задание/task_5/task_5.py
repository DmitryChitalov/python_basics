"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
try:
    with open("my_file.txt", 'w', encoding='utf-8') as file:
        file.write(' '.join(map(str, numbers)))
    with open("my_file.txt", 'r', encoding='utf-8') as file:
        numbers = file.readline()
        print(f'Сумма чисел в файле = {sum(int(x) for x in numbers.split())}')
except IOError:
    print("Ошибка ввода-вывода!")
