"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
try:
    with open("less5_t5_dig.txt", "w", encoding='utf-8') as f_numb:
        line = input("Ввод чисел через пробел: ")
        f_numb.writelines(line)
        numbers = line.split()
        print(sum(map(int, numbers)))
except IOError:
    print("Ошибка ввода/вывода")