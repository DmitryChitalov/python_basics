"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

try:
    with open('file_5.txt', 'w') as f_obj:
        line = input('Введите цифры через пробел \n')
        f_obj.writelines(line)
        num = line.split()
        print(sum(map(int, num)))
except IOError:
    print('Ошибка в файле')
except ValueError:
    print('Неправильно набран номер. Ошибка ввода-вывода')
