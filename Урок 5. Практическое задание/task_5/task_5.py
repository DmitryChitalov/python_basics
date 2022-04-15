"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

def summary():
    try:
        with open('task_5.txt', 'w+') as perf:
            line = input('Введите цифры через пробел \n')
            perf.writelines(line)
            my_numbers = line.split()

            print(sum(map(int, my_numbers)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Некорректные данные!')


summary()