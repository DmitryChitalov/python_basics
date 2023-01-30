"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
try:
    with open("numb_list.txt", "w+", encoding='utf-8') as f_numb:
        line = input("Введите числа через пробел: ")
        f_numb.writelines(line)
        numbers = line.split()
        print(sum(map(int, numbers)))
except IOError:
    print("Ошибка ввода/вывода")
except ValueError:
    print("Необходимо вводить только числа!")